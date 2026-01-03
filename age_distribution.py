import matplotlib.pyplot as plt
import pandas as pd

# Sample age data (you can change these numbers)
ages = [18, 20, 22, 22, 23, 25, 25, 25, 30, 32, 35, 40, 45, 50, 55]

# Convert list to DataFrame
df = pd.DataFrame(ages, columns=["Age"])

# Create histogram
plt.hist(df["Age"], bins=6)
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.title("Age Distribution of Population")

# Show chart
plt.show()

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
