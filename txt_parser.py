# ---------------------------------------------------------------------------
#  
# Author: Jacob Penney
# script process: 
#   1) Parse label input from txt file given at end of JABREF pipeline
#   2) create lists of labels to send to github api
#   3) send labels to github api in http request
# 
# ---------------------------------------------------------------------------




# TODO:
    # 1. add provision to accept first value of each row as issue number
        # might allow us to rethink algorithm
            # e.g. 

    # 2. implement api calls
    # 3. clean up variable names




from sys import argv




# ---------------------------------------------------------------------------
# Function: driver
# Process: accepts input file; opens, reads, and parses contents; creates
#          metalist of labels to send to github api; and calls to github api
# Parameters: accepts name of input file at command line 
# Postcondition: appropriate labels are applied to corresponding issues on
#                github
# Exceptions: none
# Note: none       
# ---------------------------------------------------------------------------
def main():

    fileToOpen = argv[1]

    # get metalist of inputs
    api_input_list = create_input_list( fileToOpen )

    print("\nList of lists of inputs:")
    for list in api_input_list:
        print( list )
    print()


    # create dictionary of labels
    label_dictionary = create_dictionary( api_input_list )
    print( "\n Dictionary of labels:" )
    print( label_dictionary )
    print()



    # create metalist of labels to send to github api
    # parse_input_lists( api_input_list, label_dictionary )




# ---------------------------------------------------------------------------
# Function: create_dictionary
# Process: uses the first row in the JABREF input text file to create
#          a dictionary which can be referenced to retrieve labels based upon
#          the index of the input argument, e.g. a value of "1" in the first
#          slot or a row will indicate to send the first label in the label
#          row
# Parameters: list of lists of input data
# Postcondition: returns a dictionary of the contents of the label row  
# Exceptions: none 
# Note: none 
# ---------------------------------------------------------------------------
def create_dictionary( input_list ):
    
    # variables
    label_dict = {}
    label_index = 0
    label_list = input_list[0]


    # loop through every item in list of first row of input file
    while label_index < len( label_list ):
        
        # assign values from first row to dictionary with corresponding index
        label_dict[label_index] = label_list[label_index]
        label_index += 1


    return label_dict




# ---------------------------------------------------------------------------
# Function: create_input_list 
# Process: accepts the name of a file to open, opens the file, reads it's
#          contents out, and processes that content into a list of lists, with
#          each internal list being one row in the input file
# Parameters: name of the file to open
# Postcondition: returns a list of lists of rows of input from the input text
# Exceptions: none 
# Note: none
# ---------------------------------------------------------------------------
def create_input_list( fileToOpen ):
 
    # variables
    COMMA = ","
    NEW_LINE = "\n"
    READ = "r"
    api_list_of_rows = []


    # open file
    api_input_file_obj = open( fileToOpen, READ )

    # read contents out
    api_input_contents = api_input_file_obj.readlines()


    # read contents out of file
    for line in api_input_contents:

        # strip rows of new line characters
        newLine_stripped_line = line.strip( NEW_LINE )

        # strip lines on commas to create list of items
        line_list = newLine_stripped_line.split( COMMA )

        # appent list of inputs to metalist of inputs
        api_list_of_rows.append( line_list )


    # close file 
    api_input_file_obj.close()


    return api_list_of_rows




# ---------------------------------------------------------------------------
# Function: parse_input_lists
# Process: accepts list of lists of binary inputs and a dictionary of labels,
#          checks input lists for binary parities, and accordingly creates
#          lists of labels to send to github api
# Parameters: list of lists of binary inputs and a dictionary of labels
# Postcondition: returns lists of lists of labels to export, contextualized by
#                their corresponding issue number
# Exceptions: none
# Note: none
# ---------------------------------------------------------------------------
def parse_input_lists( input_list, label_dict ):

    # variables
    label_metalist = []


    # loop through each list in metalist
    for row in input_list:

        # reset variables on each pass
        row_index = 0
        label_list = []

        # loop through every item in each list
        while row_index < len( row ):

            # if item in list is "1", we add the corresponding label
            # from the label dictionary to the list of labels to output
            if row[row_index] == "1":
                label_list.append( label_dict[row_index] )

            row_index += 1

        # append list of labels to label metalist to output
        if len( label_list ) > 0:
            label_metalist.append( label_list )

        print( label_metalist )







# start main
if __name__ == "__main__":
    main()




























