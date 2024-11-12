import os
from mlp_generator import preprocess_and_generate_mlp
from mlp_conversion import convert_network

input_csv_path = input("Please enter the name of the .csv file for the database: ") + '.csv'

if not os.path.isfile(input_csv_path):
    print(f"The file '{input_csv_path}' was not found. Please check the path and try again.")
else:
    output_model_file = input("Please enter the name of the output file for the MLP: ")
    preprocess_and_generate_mlp(
        input_csv=input_csv_path,
        output_model=output_model_file,
    )
    output_variable = input("Please enter the name of the output variable for the conversion: ")
    convert_network(original_name=output_model_file, output_variable=output_variable)