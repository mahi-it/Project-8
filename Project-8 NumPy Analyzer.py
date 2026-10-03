import numpy as np

class NumpyOperation:

    def __init__(self):
        self.array = None

    def create_array(self, choice):

        if choice == 1:
            n = int(input("Enter the number of elements: "))

            self.array = np.array(
                input(
                    f"Enter {n} elements separated by space: "
                ).split(),
                dtype=int
            )

        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            self.array = np.array(
                input(
                    f"Enter {rows * columns} elements for the array "
                    "separated by space: "
                ).split(),
                dtype=int
            ).reshape(rows, columns)

        elif choice == 3:
            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            self.array = np.array(
                input(
                    f"Enter {layers * rows * columns} elements "
                    "separated by space: "
                ).split(),
                dtype=int
            ).reshape(layers, rows, columns)

    
    def __indexing(self):
        if self.array is None:
            print("First create an array!")
            return
        try:
            if self.array.ndim==1:
                index=int(input("Enter the index:"))
                print("The Answer is:",self.array[index])

            elif self.array.ndim==2:
                row_index=int(input("Enter row index: "))
                col_index=int(input("Enter column index: "))
                print("The Answer is:",self.array[row_index , col_index])

            else:
                layer=int(input("Enter the layer:"))
                row_index=int(input("Enter row index: "))
                col_index=int(input("Enter column index: "))
                print("The Answer is:",self.array[layer,row_index , col_index])

        except IndexError:
            print("Index is out of range")

    def indexing(self):
        self.__indexing()

    def slicing(self):
        if self.array is None:
            print("First create an array!")
            return
        try:
            if self.array.ndim==1:
                start_index=int(input("Enter the  start index:"))
                stop_index=int(input("Enter the  stop index:"))
                print("\nSliced Array:",self.array[start_index:stop_index])

            elif self.array.ndim==2:
                row_range = input( "Enter the row range (start:end): " )

                column_range = input("Enter the column range (start:end): " )

                rs, re = map(int, row_range.split(":"))
                cs, ce = map(int, column_range.split(":"))

                print("\nSliced Array:")
                print(self.array[rs:re, cs:ce])

            elif self.array.ndim == 3:

                layer_range = input( "Enter the layer range (start:end): " )

                row_range = input( "Enter the row range (start:end):")

                column_range = input("Enter the column range (start:end): " )

                ls, le = map(int, layer_range.split(":"))
                rs, re = map(int, row_range.split(":"))
                cs, ce = map(int, column_range.split(":"))

                print("\nSliced Array:")
                print(self.array[ls:le, rs:re, cs:ce])

        except ValueError:
            print("Invalid Slicing format")
    
    def second_array(self):
         if self.array is None:
            print("First create an array!")
            return None

         values = input(f"Enter {self.array.size} elements separated by space: ").split()

         if len(values) != self.array.size:
            print(f"First Create Second Array! and You must enter exactly {self.array.size} elements.")
            return None

         try:
          second = np.array(values, dtype=int).reshape(self.array.shape)

         except ValueError:
          print("Please enter only integer values.")
          return None

         print("\nOriginal array:")
         print(self.array)

         print("\nSecond array:")
         print(second)

         return second
        

    @classmethod
    def welcome(cls):
        print("\nWelcome to the NumPy Analyzer!")
        print("===================================")


    @staticmethod
    def operation_menu():
        print("\nSelect the Type:")
        print("1.1D Array")
        print("2.2D Array ")
        print("3.3D Array")
        


obj = NumpyOperation()

NumpyOperation.welcome()

while(True):
    print("\nchoose an option:")
    print("1.Create a Numpy Array")
    print("2.Perform Mathematical Operation")
    print("3.Combine or split Arrays")
    print("4.Search,Sort,or Filter Arrays")
    print("5.Compute Aggregates and Statistics")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    match(choice):
        case 1:
                NumpyOperation.operation_menu()
                choice=int(input("Enter your choice:"))
  
                obj.create_array(choice)

                print("\nArray created successfully:")
                print(obj.array)

                while(True):
                    print("\n1.Indexing")
                    print("2.Slicing")
                    print("3.Go Back to Main Menu")
                    choice=int(input("Enter your choice:"))
                    match(choice):
                        case 1:
                            obj.indexing()
                        case 2:
                            obj.slicing()
                        case 3:
                            print("Moving back to main menu\n")
                            break
                        case _:
                            print("Invalid choice")

        case 2:
            while(True):
                print("\nchoose a mathematical operation:")
                print("1.Addition")
                print("2.Subtraction")
                print("3.Multiplication")
                print("4.Divison")
                print("5.Go Back to Main Menu")
                choice=int(input("Enter your choice:"))
                
                match(choice):
                    case 1:
                        second=obj.second_array()
                        if second is not None:
                            answer=obj.array + second
                            print("\nAddition: ",answer)
                        else:
                            print("Otherwise Addition operation will not be performed")
                    case 2:
                        second=obj.second_array()
                        if second is not None:
                            answer=obj.array - second
                            print("\nSubtraction: ",answer)
                        else:
                            print("Otherwise Subtraction operation will not be performed")
                    case 3:
                        second=obj.second_array()
                        if second is not None:
                            answer=obj.array * second
                            print("\nMultiplication: ",answer)
                        else:
                            print("Otherwise Multiplication operation will not be performed")
                    case 4:
                        second=obj.second_array()
                        if second is not None:
                            answer=obj.array / second
                            print("\nDivision: ",answer)
                        else:
                            print("Otherwise Division operation will not be performed")
                    case 5:
                        print("Moving Back to Main Menu")
                        break
                    case _:
                        print("Invalid choice")
                                     
        case 3:
            while(True):
                print("\nchoose an option:")
                print("1.Combined Array")
                print("2.Split Array")
                print("3.Go Back to Main Menu")
                choice=int(input("Enter your choice:"))

                match(choice):
                    case 1:
                        second=obj.second_array()
                        if obj.array.ndim==1:
                            print("\nCombined Array is :",np.concatenate((obj.array,second)))
                        else:
                            print("\nCombined Array(Vertical Stack):",np.vstack((obj.array,second)))

                            print("\nCombined Array(horizontal Stack):",np.hstack((obj.array,second)))
                    case 2:
                            number = int(input("Enter in how many ways you want to split: "))
                            arr = np.array(obj.array)

                            if obj.array.ndim == 1:
                                split_arr = np.array_split(arr, number)
                                print("Split Arrays:")
                                print(split_arr)

                            else:
                                try:
                                    print("\nHorizontal Split:")
                                    print(np.hsplit(arr, number))
                                except ValueError:
                                    print("\nHorizontal split is not possible.")
                                    print("Number of columns must be divisible by", number)

                                try:
                                    print("\nVertical Split:")
                                    print(np.vsplit(arr, number))
                                except ValueError:
                                    print("\nVertical split is not possible.")
                                    print("Number of rows must be divisible by", number)

                    case 3:
                            print("Moving Back to Main Menu")
                            break
                    case _:
                            print("Invalid choice")
        case 4:
            while(True):
                print("\nchoose an option:")
                print("1.Search a value")
                print("2.Sort the array")
                print("3.Filter values")
                print("4.Go Back to Main Menu")
                choice=int(input("Enter your choice:"))
                match(choice):
                    case 1:
                        value = int(input("Enter value to search: "))
                        index = np.argwhere(obj.array == value)
                        if len(index) == 0:
                           print(f"{value} is not found in the array.")
                        else:
                         print(f"Index of {value} is :")
                         for i in index:
                            print(tuple(i))
                    case 2:
                        if obj.array.ndim==1:
                            sorted_arr = np.sort(obj.array)
                            
                        elif obj.array.ndim == 2:
                            sorted_arr = np.sort(obj.array, axis=1)

                        else:
                            sorted_arr = np.sort(obj.array, axis=2)

                        print("Sorted Array:", sorted_arr)


                    case 3:
                        value=int(input("Enter the value to find the greater number from that value:"))
                        mask = obj.array > value
                        filtered_arr = obj.array[mask]

                        print("Original Array:", obj.array)
                        print("Boolean Mask:", mask)
                        print("Filtered Array:", filtered_arr)
                    case 4:
                        print("Moving Back to Main Menu")
                        break

                    case _:
                        print("Invalid choice")

        case 5:
            while(True):
                print("\nChoose an aggregate/Statistical operation:")
                print("1.sum")
                print("2.Mean")
                print("3.Median")
                print("4.Standard Deviation")
                print("5.Variance")
                print("6.Go Back to Main Menu")
                choice=int(input("Enter your choice:"))
                match(choice):
                    case 1:
                        print("Sum:",np.sum(obj.array)) 

                    case 2:
                        print("Mean:",np.mean(obj.array))
                    case 3:
                        print("Median:",np.median(obj.array))
                    case 4:
                        print("Standard Deviation:",np.std(obj.array))
                    case 5:
                        print("Variance:",np.var(obj.array))
                    case 6:
                        print("Going Back to Main Menu")
                        break
                    case _:
                        print("Invalid choice")
        case 6:
            print("Thank you for using the Numpy Analyzer! Goodbye!")
            break
        case _:
            print("Invalid choice! Please choose between 1-6")
