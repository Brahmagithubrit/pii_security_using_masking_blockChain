import pandas as pd

# Since I can't run advanced data extraction, let's create a sample dataset of names.
# I'll generate a simple list of fictional names with serial numbers for your model training.

# Sample data
sample_data = {
    "serial_no": range(1, 21),  # Serial numbers from 1 to 20
    "name": [
        "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", 
        "Robert Brown", "Linda Wilson", "David Miller", "Susan Moore", 
        "James Taylor", "Patricia Anderson", "William Thomas", 
        "Mary Jackson", "Charles Harris", "Barbara Clark", 
        "Christopher Rodriguez", "Elizabeth Lewis", "Joseph Lee", 
        "Margaret Walker", "Thomas Hall", "Sarah Young"
    ]
}

# Create DataFrame
df_sample = pd.DataFrame(sample_data)

# Save to Excel
output_path = "/mnt/data/sample_student_names.xlsx"
df_sample.to_excel(output_path, index=False)

output_path
