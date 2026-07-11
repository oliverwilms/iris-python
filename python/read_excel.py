import pandas as pd
import os

def read_excel_sheets(file_path, sheets=None):
    """
    Reads data from an Excel file.
    
    :param file_path: Path to the Excel file (.xlsx, .xls, .xlsm)
    :param sheets: None for all sheets, list of sheet names or indices for specific sheets
    :return: Dictionary {sheet_name: DataFrame}
    """
    # Validate file existence
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Read all sheets if sheets=None, else read only specified sheets
        data = pd.read_excel(file_path, sheet_name=sheets)
        return data
    except ValueError as e:
        raise ValueError(f"Error reading Excel file: {e}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Example file path (replace with your actual file)
    excel_file = r"C:\Users\olive\OneDrive\12NEW\Miles_2026.xlsx"

    # 1️⃣ Read ALL sheets
    try:
        all_sheets_data = read_excel_sheets(excel_file)
        print("=== All Sheets ===")
        for sheet, df in all_sheets_data.items():
            print(f"\nSheet: {sheet}")
            print(df.head())  # Show first 5 rows
    except Exception as e:
        print(e)

    # 2️⃣ Read SPECIFIC sheets by name
#    try:
#        selected_sheets_data = read_excel_sheets(excel_file, sheets=["Sheet1", "Sheet3"])
#        print("\n=== Selected Sheets ===")
#        for sheet, df in selected_sheets_data.items():
#            print(f"\nSheet: {sheet}")
#            print(df.head())
#    except Exception as e:
#        print(e)

    # 3️⃣ Read SPECIFIC sheets by index (0-based)
#    try:
#        index_sheets_data = read_excel_sheets(excel_file, sheets=[0, 2])
#        print("\n=== Sheets by Index ===")
#        for sheet, df in index_sheets_data.items():
#            print(f"\nSheet: {sheet}")
#            print(df.head())
#    except Exception as e:
#        print(e)
