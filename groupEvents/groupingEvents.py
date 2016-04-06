import json
# good_P1 = []
# good_P2 = []
# good_P3 = []
# good_P4 = []
# error_P1 = []
# error_P2 = []
# error_P3 = []
# error_P4 = []
# These list names correspond to the nested lists below:
# lists = [good_P1, good_P2, good_P3, good_P4, error_P1, error_P2, error_P3, error_P4]
lists = [[], [], [], [], [], [], [], []]

def groupEvents(arrayName, arrayValues, num):
        bufferList = []
        del bufferList[:]

        # We probably don't need this output array we used for testing:
        # output = []
        nxt = 0;
        # Now, go through the given list:
        for i in range(len(arrayValues)):
                
                # Current is the NUMBER WE ARE DEALING WITH
                current = arrayValues[i]
                
                # FIRST: What if there's no values? We just need to gtfo of here and leave the list empty.
                if (len(arrayValues) == 0):
                        print("This is an empty list!")
                        break
                # NEXT: If there's only one value, just print it to the appropriate list
                elif (len(arrayValues) == 1):
                        print("there's only one value and it is", current)
                        lists[num].append(current)
                        break
                # NEXT: All the logic cases.

                # a) If the first number (index 0) is unrelated to the second (index 1), just print the first number in the
                # output since it doesn't need to be buffered. If it does need to be buffered, it will be taken care of when 
                # index 1 is evaluated on the next iteration of the for loop.

                elif i == 0 and ((current+2) <= arrayValues[i+1]):
                        lists[num].append(current)
                
                # Then, for all numbers that aren't the first number:
                else:
                        # Put the previous value in the list in a variable to make this all easier to deal with.
                        prev = arrayValues[i-1]

                        # Make ourselves a variable for the next value as well, as long as we're not on the last item in the list:
                        if i != len(arrayValues)-1:
                                nxt = arrayValues[i+1]

                        # First, check if there is a buffer. 

                        # If there ISN'T a buffer: 
                        if not bufferList:
                                # First, check that we're not on the last item. 
                                if (i+1 != len(arrayValues)): 
                                        # If we're not, and the next value isn't related to the current one:
                                        if (current+2 <= nxt) and (current-2 >= prev):
                                        # Just append the current value to the output on its own.
                                                lists[num].append(current)
                                # However, if we *are* on the last value:
                                elif i == (len(arrayValues))-1:
                                        # Check if it's related to the previous value. If it's not ...
                                        if (prev+2) < current:
                                                # ... just append it to the output on its own.
                                                lists[num].append(current)
                                        # But if it's related to the previous value ...
                                        elif (prev+2) > current:
                                                # Append the current value to the buffer.
                                                bufferList.append(current)
                                                # Since this must end the buffer (there's no more values in the list), count up the number of
                                                # things in the buffer and append that value to the buffer as the last thing in the list
                                                bufferList.append(len(bufferList))
                                                # Finally, append the buffer to the output
                                                lists[num].append(bufferList)
                                                # AND THAT'S A WRAP
                                                break                           
                                # we need to evaluate whether the current value should start one by looking at the next value. 
                                if prev > current-2:
                                        bufferList.append(arrayValues[i-1])

                        # If there IS a buffer, we need to see if we need to continue it or close it off.
                        if bufferList:
                                # If this value is related to the previous value ...
                                if (prev) > current-2:
                                        # It belongs in the buffer, so append it.
                                        bufferList.append(current)
                                # If this value is not related to the previous value ...
                                else:
                                        # Then the buffer is finished. Append the number of items to the end of the buffer.
                                        bufferList.append(len(bufferList))
                                        # Next - and this took me awhile to figure out - copy the bufferList to a variable called temp.
                                        # For posterity, here's why - Python passes by reference. This means if we just append the buffer to the 
                                        # output, clear it and start again, that *also clears the instance we just appended to the output as well.*
                                        # A good way around this is to copy as a list (using list()) to a temp value, so it doesn't change.
                                        # Anyway:
                                        temp = list(bufferList)
                                        # Append that temp list to the outputName.
                                        lists[num].append(temp)
                                        # Clear the buffer
                                        del bufferList[:]
                                        # Then, check if this is the last value. If it is ...
                                        if i == (len(arrayValues)-1):
                                                # And it's unrelated to the previous value ...
                                                if (prev+2 < current):
                                                        # then it's definitely on its own. Append it to the output as a single value.
                                                        lists[num].append(current)
                                        # if current *isn't* the last value,
                                        else:
                                                # check if it's related to the NEXT value. 
                                                if (current > nxt-2) and (current != len(arrayValues)-1):
                                                        # If it is, just continue without doing anything ... we'll get it in the buffer 
                                                        # on the next iteration 
                                                        continue
                                                # If it isn't related to the next value ...
                                                elif (current <= nxt-2) and (current != len(arrayValues)-1):
                                                        # Then it's a value on its own, not in any buffer. Append to the output as a single value.
                                                        lists[num].append(current)


# with open('results_by_second.json') as json_file:
with open('results_by_second.json') as json_file:
        # load the data:
        json_data = json.load(json_file)
        json_length = len(json_data)
        # output = open('results_groupedEvents.txt', 'w+')
        output = open('testOutput_bySecond.txt', 'w+')
        output.write('[')
        count = json_length
        print("starting processing ...")
        for entry in json_data:
                # first, print the opening bracket to contain this unit of json data.
                output.write('\n{')
                if 'group' in entry:
                        # print("group number:",entry['group'])
                        output.write('\n\t"group":'+ str(entry['group'])+',')
                if 'error_P1' in entry:
                        del lists[4][:]
                        # print("sending errors from P1 ...")
                        groupEvents('error_P1', entry['error_P1'], 4)
                if 'error_P2' in entry:
                        del lists[5][:]
                        # print("sending errors from P2 ...")
                        groupEvents('error_P2', entry['error_P2'], 5)
                if 'error_P3' in entry:
                        del lists[6][:]
                        # print("sending errors from P3 ...")
                        groupEvents('error_P3', entry['error_P3'], 6)
                if 'error_P4' in entry:
                        del lists[7][:]
                        # print("sending errors from P4 ...")
                        groupEvents('error_P4', entry['error_P4'], 7)
                if 'good_P1' in entry:
                        del lists[0][:]
                        # print("sending errors from P1 ...")
                        groupEvents('good_P1', entry['good_P1'], 0)
                if 'good_P2' in entry:
                        del lists[1][:]
                        # print("sending errors from P2 ...")
                        groupEvents('good_P2', entry['good_P2'], 1)
                if 'good_P3' in entry:
                        del lists[2][:]
                        # print("sending errors from P3 ...")
                        groupEvents('good_P3', entry['good_P3'], 2)
                if 'good_P4' in entry:
                        del lists[3][:]
                        # print("sending errors from P4 ...")
                        groupEvents('good_P4', entry['good_P4'], 3)

                output.write('\n\t"good_P1":'+str(lists[0])+',')  
                output.write('\n\t"good_P2":'+str(lists[1])+',')
                output.write('\n\t"good_P3":'+str(lists[2])+',')
                output.write('\n\t"good_P4":'+str(lists[3])+',')
                output.write('\n\t"error_P1":'+str(lists[4])+',')  
                output.write('\n\t"error_P2":'+str(lists[5])+',')
                output.write('\n\t"error_P3":'+str(lists[6])+',')
                output.write('\n\t"error_P4":'+str(lists[7])+',')
                # print the participants' user name:
                output.write('\n\t"ident":"'+ (entry['ident'])+'"')
                # print the closing bracket
                output.write('\n},\n')
        output.write('\n]')
        print("processing finished!")