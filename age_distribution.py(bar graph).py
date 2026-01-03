import matplotlib.pyplot as plt
import pandas as pd

# Sample gender data
genders = ["Male", "Female", "Female", "Male", "Female", "Male", "Female"]

# Count genders
df = pd.Series(genders).value_counts()

# Create bar chart
df.plot(kind="bar")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")

plt.show()
