import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x_food_qual = np.arange(0, 11, 1)
x_service_qual = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)

# Define membership functions for 'quality'
qual_lo = fuzz.trimf(x_food_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_food_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_food_qual, [5, 10, 10])

# Define membership functions for 'service'
serv_lo = fuzz.trimf(x_service_qual, [0, 0, 5])
serv_md = fuzz.trimf(x_service_qual, [0, 5, 10])
serv_hi = fuzz.trimf(x_service_qual, [5, 10, 10])

# Define membership functions for 'tip'
tip_lo = fuzz.trimf(x_tip, [0, 0, 10])
tip_md = fuzz.trimf(x_tip, [0, 10, 20])
tip_hi = fuzz.trimf(x_tip, [10, 20, 25])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_food_qual, qual_lo, 'b', linewidth=1.5, label='Poor')
ax0.plot(x_food_qual, qual_md, 'g', linewidth=1.5, label='Average')
ax0.plot(x_food_qual, qual_hi, 'r', linewidth=1.5, label='Excellent')
ax0.set_title('Food Quality')
ax0.legend()

ax1.plot(x_service_qual, serv_lo, 'b', linewidth=1.5, label='Poor')
ax1.plot(x_service_qual, serv_md, 'g', linewidth=1.5, label='Average')
ax1.plot(x_service_qual, serv_hi, 'r', linewidth=1.5, label='Excellent')
ax1.set_title('Service Quality')
ax1.legend()

ax2.plot(x_tip, tip_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_tip, tip_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_tip, tip_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('Tip Amount')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!
food_qual_level_lo = fuzz.interp_membership(x_food_qual, qual_lo, 6.5)
food_qual_level_md = fuzz.interp_membership(x_food_qual, qual_md, 6.5)
food_qual_level_hi = fuzz.interp_membership(x_food_qual, qual_hi, 6.5)
service_qual_level_lo = fuzz.interp_membership(x_service_qual, serv_lo, 9.8)
service_qual_level_md = fuzz.interp_membership(x_service_qual, serv_md, 9.8)
service_qual_level_hi = fuzz.interp_membership(x_service_qual, serv_hi, 9.8)

# Now we take our rules and apply them. Rule 1 concerns poor food OR service.
# The OR operator means we take the maximum of these two.
active_rule1 = np.fmax(food_qual_level_lo, service_qual_level_lo)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`
tip_activation_lo = np.fmin(active_rule1, tip_lo)  # removed entirely to 0

# For rule 2 we connect acceptable service to medium tipping
tip_activation_md = np.fmin(service_qual_level_md, tip_md)

# For rule 3 we connect high service OR high food with high tipping
active_rule3 = np.fmax(food_qual_level_hi, service_qual_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)

tip0 = np.zeros_like(x_tip)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.fill_between(x_tip, tip0, tip_activation_lo, facecolor='b', alpha=0.7)
ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_tip, tip0, tip_activation_md, facecolor='g', alpha=0.7)
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, tip_activation_hi, facecolor='r', alpha=0.7)
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# Aggregate all three output membership functions together
aggregated = np.fmax(tip_activation_lo,
                     np.fmax(tip_activation_md, tip_activation_hi))
# Calculate defuzzified result
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()