import openpyxl
import os
import sys

def iterate_excel_all_sheets(file_path):
    """
    Iterates over all sheets in an Excel file and prints non-empty cells.
    :param file_path: Path to the Excel file (.xlsx)
    """
    try:
        # Validate file existence
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Validate file extension
        if not file_path.lower().endswith(".xlsx"):
            raise ValueError("Only .xlsx files are supported.")

        # Load workbook
        workbook = openpyxl.load_workbook(file_path, data_only=True)

        # Loop through all sheets
        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
            print(f"\n--- Sheet: {sheet_name} ---")

            # Iterate over all rows and cells
            for row in sheet.iter_rows():
                for cell in row:
                    # Skip empty cells (None or empty string after stripping)
                    if cell.value is None:
                        continue
                    if isinstance(cell.value, str) and cell.value.strip() == "":
                        continue

                    print(f"Cell {cell.coordinate}: {cell.value}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    excel_file = r"C:\Users\olive\OneDrive\12NEW\Miles_2026.xlsx"
    iterate_excel_all_sheets(excel_file)
