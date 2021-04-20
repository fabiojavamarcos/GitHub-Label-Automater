####################
#  
# Author: Jacob Penney
# script process: 
#   1) Parse label input from txt file given at end of JABREF pipeline
#   2) create lists of labels to send to github api
#   3) send labels to github api in http request
# 
#################### 



# TODO:
    # fix parse_input_lists
    # implement api calls



# imports
from sys import argv


def main():

    fileToOpen = argv[1]

    api_input_list = create_input_list( fileToOpen )
    # print("\nList of lists of inputs:")
    # for list in api_input_list:
    #     print( list )
    # print()

    label_dictionary = create_dictionary( api_input_list )
    # print( "\n Dictionary of labels:" )
    # print( label_dictionary )
    # print()


    parse_input_lists( api_input_list, label_dictionary )




def create_dictionary( input_list ):
    
    label_dict = {}
    label_index = 0
    label_list = input_list[0]


    while label_index < len( label_list ):
        label_dict[label_index] = label_list[label_index]
        label_index += 1

    return label_dict




def create_input_list( fileToOpen ):
 
    COMMA = ","
    NEW_LINE = "\n"
    READ = "r"
    api_list_of_rows = []


    # open file
    api_input_file_obj = open( fileToOpen, READ )
    
    # get contents of file
    api_input_contents = api_input_file_obj.readlines()

    # parse lines
    for line in api_input_contents:

        newLine_stripped_line = line.strip( NEW_LINE )

        line_list = newLine_stripped_line.split( COMMA )

        api_list_of_rows.append( line_list )

    # close file
    api_input_file_obj.close()


    return api_list_of_rows




def parse_input_lists( input_list, label_dict ):

    label_metalist = []

    for row in input_list:
        row_index = 0
        label_list = []

        while row_index < len( row ):
            if row[row_index] == "1":
                label_list.append( label_dict[row_index] )


            row_index += 1

        label_metalist.append( label_list )
        # print( label_list )

    # print( label_metalist )






# start main
if __name__ == "__main__":
    main()




























