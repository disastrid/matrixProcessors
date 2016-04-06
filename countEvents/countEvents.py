import json

def countEvents(arrayName, arrayValues):
        listLen = len(arrayValues)
        output.write('\n\t"'+arrayName+'":'+str(listLen)+',')  



with open('grouped_events.json') as json_file:
        # load the data:
        json_data = json.load(json_file)
        json_length = len(json_data)
        # output = open('results_groupedEvents.txt', 'w+')
        output = open('countedEvents.txt', 'w+')
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
                        countEvents('error_P1', entry['error_P1'])
                if 'error_P2' in entry:
                        countEvents('error_P2', entry['error_P2'])
                if 'error_P3' in entry:
                        countEvents('error_P3', entry['error_P3'])
                if 'error_P4' in entry:
                        countEvents('error_P4', entry['error_P4'])
                if 'good_P1' in entry:
                        countEvents('good_P1', entry['good_P1'])
                if 'good_P2' in entry:
                        countEvents('good_P2', entry['good_P2'])
                if 'good_P3' in entry:
                        countEvents('good_P3', entry['good_P3'])
                if 'good_P4' in entry:
                        countEvents('good_P4', entry['good_P4'])

                # print the participants' user name:
                output.write('\n\t"ident":"'+ (entry['ident'])+'"')
                # print the closing bracket
                output.write('\n},\n')
        output.write('\n]')
        print("processing finished!")