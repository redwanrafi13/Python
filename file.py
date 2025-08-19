class employee:
    def __init__(self,emp_id,name,hourly_rate):
        self.emp_id=emp_id
        self.name=name
        self.hourly_rate=hourly_rate
        self.hours_worked=0
        
    def set_work_hour(self,hour):
        self.hours_worked=hours
        
    def calculate_salary(self):
        self.hours_worked * hourly_rate
        
    def display_info(self):
        print(f"employee_id     :{self.emp_id}")
        print(f"name            :{self.name}")
        print(f"type            :{self.get_employee_type()}")
        print(f"hours worked    :{self.hours_worked}")
        print(f"hourly rate     :{self.hurly_rate}")
        print(f"total salary    :{self.calculate_salary()} taka/n")
        
    def get_employee_type(self):
        return "general employee"
class regularemployee(employee):
    def calculate_salay(self):
        base_salary=super().calculate_salary
        if self.hours_worked > 160:
            bonus= 0.10 * base_salary
            return base_salary + bonus
        return base_salary
    
    def calculate_overtime_bonus(self):
        if self.hours_worked > 160:
            bonus= 0.10 *(self.hours_worked * self.hourly_rate)
            print(f"[note] overtime bonus: {bonus:.2f} taka")
        else:
            print("[note] no overtime bonus")
            
    def get_employee_type(self):
        return "regular employee"
    
class temporaryemployee(employee):
    def cheak_max_hours(self):
        if self.hours_worked >120:
            print("[warning] temporary employee exceeded 120 working hour")
            print()
        else:
            print([note]working hours within the permitted limit.)
            print()
            
    def get_employee_type(self):
        return "temporary employee"
    
if __name__=="__main__":
    emp1=regularemployee(emp_id=301,name="mahmudullah riyad", hourly_rate=300)
    emp2=temporaryemployee(emp_id=302,name="soumya sarkar",hourly_rate=200)
    emp3=regularemployee(emp_id=303,name="tamim iqbal,"hourly_rate=200)