class MobilePhone:
    def __init__(self, name, number, operator, apps):
        self.name = name
        self.number = number
        self.operator = operator
        self.apps = apps

    def find_operator(self):
        operator_msg = f'{self.operator} is the operator for {self.name}'
        return operator_msg
        
        

daniels_iphone12_pro =  MobilePhone("daniels_iphone12_pro", 123_456_789, "vodafone", ["settings", "clock", "instagram", "spotify"])

print(daniels_iphone12_pro.find_operator())