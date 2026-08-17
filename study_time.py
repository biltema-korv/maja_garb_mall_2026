import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Matcha figurens typsnitt och storlek mot LaTeX-dokumentet
# (fontsize: 10pt, geometry: margin=1in => textbredd 6.5in, se garb.qmd).
# Använder samma Latin Modern-typsnitt som dokumentet, buntat i fonts/.
for _f in ("lmroman10-regular.otf", "lmroman10-bold.otf", "lmroman10-italic.otf"):
    fm.fontManager.addfont(f"fonts/{_f}")

plt.rcParams.update({
    "font.family": "Latin Modern Roman",
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
})

# Samma färg, linjebredd och handritade "sketch"-linjer som de andra
# figurerna, för ett enhetligt utseende genom hela rapporten.
LINE_COLOR = "#2f5f9e"
AXIS_LW = 1.0
SKETCH = dict(scale=0.45, length=170, randomness=1)

def sketch_spines(ax):
    for spine in ax.spines.values():
        spine.set_linewidth(AXIS_LW)
        spine.set_sketch_params(**SKETCH)

# Mock data
study_time = np.array([0, 1, 2, 3, 4])
grades = ['E', 'D', 'C', 'B', 'A']
grade_numeric = np.array([1, 2, 3, 4, 5])

# Create line graph (motsvarande tidigare 80% av textbredden, nu satt
# direkt; inkludera i LaTeX med width=5.2in för att matcha exakt)
fig, ax = plt.subplots(figsize=(5.2, 3.9))
ax.set_axisbelow(True)
ax.grid(True, which='major', color='#a9c4e0', linewidth=0.5, alpha=0.4)

line, = ax.plot(study_time, grade_numeric, linestyle='-', linewidth=1.6, color='black', zorder=2)
line.set_sketch_params(scale=0.45, length=110, randomness=2)
ax.scatter(study_time, grade_numeric, s=60, facecolor=LINE_COLOR, edgecolor='black',
           linewidth=AXIS_LW, zorder=3)
sketch_spines(ax)

# Customize the chart
ax.set_xlabel('Studietid (timmar/dag)')
ax.set_ylabel('Betyg')
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(0.5, 6.5)

# Customize x-axis ticks
ax.set_xticks(study_time)

# Customize y-axis ticks
ax.set_yticks(grade_numeric, grades)

# Add labels to each point
for x, y, grade in zip(study_time, grade_numeric, grades):
    ax.text(x, y + 0.25, grade, ha='center', va='bottom', fontweight='bold')

# Improve layout
plt.tight_layout()

# Save the figure
plt.savefig('study_time.pdf')
plt.close()