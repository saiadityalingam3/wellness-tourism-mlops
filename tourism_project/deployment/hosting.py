
import os

print("Deployment files are ready.")

print("\nFiles available for deployment:")

for file in os.listdir("tourism_project/deployment"):
    print(file)

print("\nUpload these files to your Hugging Face Space:")
print("- app.py")
print("- requirements.txt")
print("- Dockerfile")
