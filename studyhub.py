# StudyHub Data Indexer Engine - Team Code Chaos

materials_database = {
    "26CS101": ["Unit 1 - C Program Basics.pdf", "Unit 2 - Control Statement.pdf", "Model Paper 2025.pdf"],
    "26MA101": ["Unit 1 - Calculas and linear algebra.pdf", "Unit 2 - Multiple Integrals.pdf"],
    "26EC101": ["Unit 1 - Digital Principles.pdf"],
    "26HS102" :["Unit 1 - Universal Human Value.pdf"],
    "26CS102" :["Unit 1 - Foundation of Full Stack.pdf"]
}

def search_materials(subject_code):
    subject_code = subject_code.upper()
    if subject_code in materials_database:
        print(f"\n--- Found resources for {subject_code} ---")
        for idx, item in enumerate(materials_database[subject_code], 1):
            print(f"{idx}. {item}")
    else:
        print(f"\nNo notes found for {subject_code}. Be the first to upload!")

if __name__ == "__main__":
    print("=== StudyHub Backend Processing Engine ===")
    code = input("Enter Subject Code to search (e.g., 26CS101): ")
    search_materials(code)
