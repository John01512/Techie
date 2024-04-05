import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Generate universe variables
x_food_qual = np.arange(0, 11, 1)
x_service_qual = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)

# Generate fuzzy membership functions
qual_lo = fuzz.trimf(x_food_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_food_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_food_qual, [5, 10, 10])

serv_lo = fuzz.trimf(x_service_qual, [0, 0, 5])
serv_md = fuzz.trimf(x_service_qual, [0, 5, 10])
serv_hi = fuzz.trimf(x_service_qual, [5, 10, 10])

tip_lo = fuzz.trimf(x_tip, [0, 0, 10])
tip_md = fuzz.trimf(x_tip, [0, 10, 20])
tip_hi = fuzz.trimf(x_tip, [10, 20, 25])

# Visualize universes and membership functions
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
plt.show()

# Aggregation and defuzzification
food_qual_level_lo = fuzz.interp_membership(x_food_qual, qual_lo, 6.5)
food_qual_level_md = fuzz.interp_membership(x_food_qual, qual_md, 6.5)
food_qual_level_hi = fuzz.interp_membership(x_food_qual, qual_hi, 6.5)

service_qual_level_lo = fuzz.interp_membership(x_service_qual, serv_lo, 9.8)
service_qual_level_md = fuzz.interp_membership(x_service_qual, serv_md, 9.8)
service_qual_level_hi = fuzz.interp_membership(x_service_qual, serv_hi, 9.8)

active_rule1 = np.fmax(food_qual_level_lo, service_qual_level_lo)
tip_activation_lo = np.fmin(active_rule1, tip_lo)

tip_activation_md = np.fmin(service_qual_level_md, tip_md)

active_rule3 = np.fmax(food_qual_level_hi, service_qual_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)

tip0 = np.zeros_like(x_tip)

aggregated = np.fmax(tip_activation_lo,
                     np.fmax(tip_activation_md, tip_activation_hi))
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)

# Visualize
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)

ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.get_xaxis().tick_bottom()
ax0.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
