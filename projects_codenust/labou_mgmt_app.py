class LabourApp:

    def __init__(self):
        # initialize labour first
        self.labours = []

    # adding method > new labour
    def add(self, name, age, skill, wage):
        self.labours.append({
            "name": name,
            "age": age, 
            "skill": skill, 
            "wage": wage, 
            "days": 0
        })
        print(f"✅ Added {name} successfully!")

    # work method > record one day of work
    def work(self, name):
        for labour in self.labours:
            if labour['name'] == name:
                labour["days"] += 1
                print(f"💪 {name} worked a day. Total days: {labour['days']}")
                return
        print(f"❌ Worker '{name}' not found!")

    # salary method > calculate salary
    def salary(self, name):
        for labour in self.labours:
            if labour['name'] == name:
                pay = labour["wage"] * labour["days"]
                print(f"💰 {name}'s Salary = ${pay}")
                return
        print(f"❌ Worker '{name}' not found!")
    
    # view method > show all labours
    def view(self):
        if not self.labours:  # Check if list is empty
            print("📭 No workers added yet!")
            return
            
        print("\n👥 All Workers:")
        print("-" * 50)
        for i, labour in enumerate(self.labours):  # 🔧 FIXED: removed .l
            print(f"{i+1}. {labour['name']} - {labour['age']}yrs - ${labour['wage']}/day - Days worked: {labour['days']} - Skill: {labour['skill']}")

    # remove method > delete labour by name
    def remove(self, name):
        original_count = len(self.labours)
        self.labours = [labour for labour in self.labours if labour['name'] != name]
        
        if len(self.labours) < original_count:
            print(f"🗑️ Removed {name} successfully!")
        else:
            print(f"❌ Worker '{name}' not found!")

# Main program
app = LabourApp()

while True:
    print("\n" + "="*40)
    print("🏗️  LABOUR MANAGEMENT SYSTEM  🏗️")
    print("="*40)
    print("1. 👤 Add Labour")
    print("2. 👥 View All Labours") 
    print("3. 💪 Record Work Day")
    print("4. 💰 Calculate Salary")
    print("5. 🗑️  Remove Labour")
    print("6. 🚪 Exit")
    print("="*40)
    
    choice = input("Choose (1-6): ").strip()

    if choice == "1":
        print("\n➕ Adding New Worker...")
        name = input("Name: ").strip()
        age = int(input("Age: "))
        skill = input("Skill: ").strip()
        wage = int(input("Wage per day ($): "))
        app.add(name, age, skill, wage)

    elif choice == "2":
        app.view()

    elif choice == "3":
        name = input("\n👤 Worker name: ").strip()
        app.work(name)

    elif choice == "4":
        name = input("\n💰 Worker name: ").strip()
        app.salary(name)

    elif choice == "5":
        name = input("\n🗑️ Worker name to remove: ").strip()
        app.remove(name)

    elif choice == "6":
        print("\n👋 Goodbye! Thanks for using Labour Management System!")
        break

    else:
        print("❌ Invalid choice! Please enter 1-6.")