from tkinter import *
import re

class Calculator(object):
    def __init__(self, master):
        # Heading
        self.master = master
        master.title("Calculator")

        # Input storing
        self.button_cache = []
        self.input_list = []
        self.input_string = ""

        # Two displays
        self.out = Text(master, height=2, width=30)
        self.out.grid(row=0, column=0, columnspan=5, sticky="news")

        self.result = Text(master, height=2, width=30)
        self.result.grid(row=1, column=0, columnspan=5, sticky="news")

        # Buttons
        self.point = Button(master, text = ".", command= lambda: self.typing("."), height=3, width=3)
        self.point.grid(row=5, column=0, sticky="news")
        self.point.bind("<Configure>", self.resize)

        self.zero = Button(master, text = "0", command=lambda: self.typing(0), height=3, width=3)
        self.zero.grid(row=5, column=1, sticky="news")

        self.neg = Button(master, text = "-", command= lambda: self.typing("N"), height=3, width=3)
        self.neg.grid(row=5, column=2, sticky="news")

        self.one = Button(master, text = "1", command= lambda: self.typing(1), height=3, width=3)
        self.one.grid(row=4, column=0, sticky="news")

        self.two = Button(master, text = "2", command= lambda: self.typing(2), height=3, width=3)
        self.two.grid(row=4, column=1, sticky="news")

        self.three = Button(master, text = "3", command= lambda: self.typing(3), height=3, width=3)
        self.three.grid(row=4, column=2, sticky="news")

        self.four = Button(master, text = "4", command= lambda: self.typing(4), height=3, width=3)
        self.four.grid(row=3, column=0, sticky="news")

        self.five = Button(master, text = "5", command= lambda: self.typing(5), height=3, width=3)
        self.five.grid(row=3, column=1, sticky="news")

        self.six = Button(master, text = "6", command= lambda: self.typing(6), height=3, width=3)
        self.six.grid(row=3, column=2, sticky="news")

        self.seven = Button(master, text = "7", command= lambda: self.typing(7), height=3, width=3)
        self.seven.grid(row=2, column=0, sticky="news")

        self.eight = Button(master, text = "8", command= lambda: self.typing(8), height=3, width=3)
        self.eight.grid(row=2, column=1, sticky="news")

        self.nine = Button(master, text = "9", command= lambda: self.typing(9), height=3, width=3)
        self.nine.grid(row=2, column=2, sticky="news")

        self.add = Button(master, text = "+", command= lambda: self.typing("+"), height=3, width=3)
        self.add.grid(row=2, column=3, sticky="news")

        self.minus = Button(master, text = "-", command= lambda: self.typing("-"), height=3, width=3)
        self.minus.grid(row=3, column=3, sticky="news")

        self.mult = Button(master, text = "X", command= lambda: self.typing("X"), height=3, width=3)
        self.mult.grid(row=4, column=3, sticky="news")

        self.div = Button(master, text = "/", command= lambda: self.typing("/"), height=3, width=3)
        self.div.grid(row=5, column=3, sticky="news")

        self.enter = Button(master, text = "=", command=self.enter, height=5, width=5)
        self.enter.grid(row = 2, column= 4, rowspan = 2, sticky="news")

        self.clear_but = Button(master, text = "C", command=self.clear, height=5, width=5)
        self.clear_but.grid(row = 4, column = 4, rowspan=2, sticky="news")

        self.inheight = 0
        print(self.master)




    def resize(self, event):
        print(event.height)
        print(event.width)
        print()



    def valid(self, comm):
        # Check if the pressed button is valid.
        if len(self.input_list) == 0:
            # First entry
            if type(comm) is int:
                return True
            elif comm in [".", "N"]:
                return True
            else:
                return False
        else:
            if type(comm) is int:
                return True
            elif comm == ".":
                if self.input_list[-1] == ".":
                    return False
                else:
                    return True
            elif comm == "N":
                if self.input_list[-1] in ["X", "/", "+", "-"]:
                    return True
                else:
                    return False
            else:
                if type(self.input_list[-1]) is int:
                    return True
                elif self.input_list[-1] == ".":
                    if type(self.input_list[-2]) is int:
                        return True
                    else:
                        return False
                else:
                    return False


    def typing(self, comm):
        # Adds entry to list and displays it.
        try:
            if self.button_cache[-1] == "E":
                self.clear()
        except IndexError:
            pass

        if self.valid(comm):
            if comm == "N":
                self.input_list.append(comm)
                self.input_string += "-"
                self.out.delete(1.0, END)
                self.out.insert(INSERT, self.input_string)
                self.button_cache.append(comm)
            else:
                self.input_list.append(comm)
                self.input_string += str(comm)
                self.out.delete(1.0, END)
                self.out.insert(INSERT, self.input_string)
                self.button_cache.append(comm)
        else:
            pass

    def enter(self):
        # Perform calculations
        try:
            if self.input_list[-1] in ["X", "/", "+", "-", "N"]:
                return
            if self.input_list[-1] == ".":
                if not self.input_list[-2] is int:
                    return
            if self.button_cache[-1] == "E":
                self.clear()
                return
        except IndexError:
            return

        operations = []
        newstring = "".join(str(x) for x in self.input_list)
        for i in range(len(newstring)):
            # Make operations list
            if newstring[i] in ["X", "/", "+", "-"]:
                operations.append(newstring[i])
            else:
                pass
        numbers = re.split("X|/|\+|-", newstring)
        for i in range(len(numbers)):
            # Change N to negative and string to float
            if numbers[i][0] == "N":
                new = "-" + numbers[i][1::]
                numbers[i] = new
            numbers[i] = float(numbers[i])

        # Now for pemdas.
        npass1 = []
        opass = []
        for i in range(len(operations)):
            if operations[i] in ["+", "-"]:
                # Append
                npass1.append(numbers[i])
                opass.append(operations[i])
                if i == len(operations) - 1:
                    npass1.append(numbers[i+1])
            else:
                if operations[i] == "X":
                    # multiply
                    res = numbers[i]*numbers[i+1]
                    npass1.append(res)
                    numbers[i+1] = res
                else:
                    # divide
                    try:
                        res = numbers[i]/numbers[i+1]
                        npass1.append(res)
                        numbers[i+1] = res

                    except ZeroDivisionError:
                        self.result.insert(INSERT, "Undefined")
                        self.button_cache.append("E")
                        return


        for i in range(len(opass)):
            if opass[i] == "-":
                #subtract
                res = npass1[i] - npass1[i+1]
                npass1[i+1] = res
            else:
                #add
                res = npass1[i] + npass1[i+1]
                npass1[i+1] = res
        if npass1[-1]%1 == 0:
            final = int(npass1[-1])
        else:
            final = npass1[-1]
        final = format(final, '.10g')
        self.result.insert(INSERT, str(final))
        self.button_cache.append("E")





    def clear(self):
        # Clears all entries.
        self.out.delete(1.0, END)
        self.result.delete(1.0, END)
        self.input_list = []
        self.input_string = ''
        self.button_cache = []



def main():
    root = Tk()
    my_gui = Calculator(root)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.mainloop()


main()