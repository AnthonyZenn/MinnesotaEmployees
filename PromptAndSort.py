#MnEmployee
#==========================================
# Purpose: Used to create and store data about employees
#
# Instance variables: employeeId: employee ID (string)
#   __salary: employee salary (privat, float)
#   __otWages: overtime wages (private, float)
#   __addWages: additional wages (private, float)
#   __totalWages: total wages, which is salary+otWages+addWages (private, float)
#
# Methods: get_salary(self): returns employee salary
#   get_otWages(self): returns overtime wages
#   get_addWages(self): returns additional wages
#   get_totalWages(self): returns total wages
#   set_salary(self, newSalary): sets employee salary to newSalary
#       will also adjust to correct totalWages
#   set_otWages(self, newOT): sets overtime wages to newOT
#       will also adjust to correct totalWages
#   set_addWages(self, newAdd): sets additional wages to newAdd
#       will also adjust to correct totalWages
#   set_totalWages(self, newTotal): sets total wages to newTotal
#       !!!! This is problematic to me because changing total wages may result
#       in the total not equalling the sum of the other wages!!!
#   __lt__(self,other) will overload less than operator to compare
#       total wages between employees
#   __gt__(self,other) will overload greater than operator to compare
#       total wages between employees
#   __repr__ this is used to print out employee attributes separated by commas
#   __str__ this is used to print out employee attributes separated nicely by whitespace
#==========================================

class MnEmployee():

    # initialize attributes of employee
    def __init__(self, employeeId="", salary=0, otWages=0, addWages=0, totalWages=0):
        self.employeeId = str(employeeId)
        self.__salary = float(salary)
        self.__otWages = float(otWages)
        self.__addWages = float(addWages)
        self.__totalWages = float(totalWages)
        #check to see if total wages makes sense
        if (abs(self.__totalWages - self.__salary - self.__otWages - self.__addWages) > 1.0):
            print("Total wages does not equal salary + overtime + additional wages")

    # return salary
    def get_salary(self):
        return self.__salary

    # return overtime wages
    def get_otWages(self):
        return self.__otWages

    # return additional wages
    def get_addWages(self):
        return self.__addWages

    # return total wages
    def get_totalWages(self):
        return self.__totalWages

    # set new salary, and adjust total wages
    def set_salary(self, newSalary):
        self.__salary = float(newSalary)
        self.__totalWages = self.__salary + self.__otWages + self.__addWages

    # set new overtime wages, and adjust total wages
    def set_otWages(self, newOT):
        self.__otWages = float(newOT)
        self.__totalWages = self.__salary + self.__otWages + self.__addWages

    # set new additional wages, and adjust total wages
    def set_addWages(self, newAdd):
        self.__addWages = float(newAdd)
        self.__totalWages = self.__salary + self.__otWages + self.__addWages

    # set new total wages, and checks total wages
    def set_totalWages(self, newTotal):
        self.__totalWages = float(newTotal)
        # check to see if total wages makes sense
        if (abs(self.__totalWages - self.__salary - self.__otWages - self.__addWages) > 1.0):
            print("Total wages does not equal salary + overtime + additional wages")

    # compare total wages between employees, first do less than
    def __lt__(self,other):
        if (self.__totalWages < other.__totalWages):
            return True
        else:
            return False

    # now do greater than
    def __gt__(self,other):
        if (self.__totalWages > other.__totalWages):
            return True
        else:
            return False

    # this is used to print employee attributes separated by commas
    def __repr__(self):
        empId = str(self.employeeId)
        sal = str(self.__salary)
        ot = str(self.__otWages)
        add = str(self.__addWages)
        tot = str(self.__totalWages)
        return (empId + ',' + sal + ',' + ot + ',' + add + ',' + tot)

    # this is used to print employee attribues separated nicely by whitespace
    def __str__(self):
        f1 = '{empID:12}' # these statements format to take up 12 character spaces
        f2 = '{sal:12}'
        f3 = '{ot:12}'
        f4 = '{add:12}'
        f5 = '{tot:12}'
        return(f1.format(empID=str(self.employeeId))+'\t'+f2.format(sal=str(self.__salary))+ \
               '\t'+f3.format(ot=str(self.__otWages))+'\t'+f4.format(add=str(self.__addWages)) \
               +'\t'+f5.format(tot=str(self.__totalWages)))

#getTotalWages
#==========================================
# Purpose: used to get total wages from an employee for sorting
# Input Parameter(s): aPerson: this is a MnEmployee object which has
#   all of the MnEmployee attributes
# Return Value(s): aPerson.get_totalWages(), which is a floating
#   point value of the employee's total wages
#==========================================
def getTotalWages(aPerson):
    return aPerson.get_totalWages()

#main
#==========================================
# Purpose: This function will prompt the user for an input file
#   and will print out the employee information in ascending or descending
#   order depending on the user's choice (the user can also choose the number
#   of employees' information to print out).  It will also output a file in csv
#   format with the information with a user chosen name if the user desires. There
#   also be some checks to deal with incorrect user inputs. There will also be a
#   continuation loop.
#
# Input Parameter(s): None, but the user will be prompted for an input file
#
# Return Value(s): None, but the program will print out employee information based on
#   some user specifications.  The program will also create a file in csv format of the
#   employee information if the user desires, with a name the user desires.
#==========================================


def main():

    # below is code to get and open input file
    input_file_opened = False
    while not input_file_opened:
        try: # this is for file opening correctly
            fileName = input("Enter input file name with extension: ")
            inputFile = open(fileName,'r')
            input_file_opened = True

        except IOError as e: # this is for file not opening correctly
            s = str(e)
            print("Error: ", s, "please re enter\n")

    #now read in file data and store in list
    empList = []
    lines = inputFile.readlines() # reads in contents

    for i in range(1,len(lines)): # start for loop at 1 to bypass header
        line = lines[i].strip() # strip whitespace
        info = line.split(',') # separates values
        empList.append(MnEmployee(info[0],info[1],info[2],info[3],info[4])) # creates object
    # end for loop
    inputFile.close()

    done = False # initialize continuation loop
    while not done:

        orderChosen = False # initialize order choice loop
        while not orderChosen: # make sure user enters valid input
            choice = input("Sort in (A)scending or (D)escending order: ")
            if choice == 'A' or choice == 'D':
                orderChosen = True
            else:
                print("ERROR: selection: ",choice," not recognized, please re-enter")
        # end while loop for order choice

        # now create sort list
        if choice == 'A': # ascending
            sortList = sorted(empList, key=getTotalWages)
        else: # descending
            sortList = sorted(empList, key=getTotalWages, reverse=True)

        recordsChosen = False # initialize record choice loop
        while not recordsChosen: # make sure user chooses valid number of records
            print("How many Employee records would you like to print?")
            numRecords = input("Enter a number between 0 and 100 : ")
            try:
                numRecords = int(numRecords)
                if numRecords <= 100 and numRecords >= 0:
                    recordsChosen = True
            except:
                print("ERROR: ",numRecords," is an invalid number of records, please re-enter")
        # end while loop for record choice
        
        print()
        print("Employee Id      Wages       Overtime         Additional         Total")

        for i in range(numRecords): # this prints out the employee records
            print(sortList[i])
        #end for loop
        print()
        
        # now see if user wants to save
        save = input("Save sorted list? (Enter 'Y' or 'y'): ")
        # make output file
        if save in ('Y','y'):
            outFile = input("Enter name of output file: ")
            o = open(outFile,'w')
            for i in range(numRecords): # writes everything to output as strings
                ID = str(sortList[i].employeeId)
                sal = str(sortList[i].get_salary())
                ot = str(sortList[i].get_otWages())
                add = str(sortList[i].get_addWages())
                tot = str(sortList[i].get_totalWages())
                o.write(ID + ',' + sal + ',' + ot + ',' + add + ',' + tot + '\n')
            #end for loop
            o.close()
                
        keepGoing = input("Enter 'Y' or 'y' to continue: ") #continuation loop check
        if keepGoing not in('Y','y'): # this will end program
            done = True
            print()
        

if __name__ == "__main__":
    main()
