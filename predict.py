
import getopt
import sys

def help_error_message():
    print "Use the -h or --help flags for help."

def usage():
    print "Usage: python predict.py [-flags] file"
    print " -h, --help: display this message"
    print " -i file, --train=file: use file as training set"
    print " -o file, --output=file: write test set predictions to file (use with the -t flag)"
    print " -t file, --test=file: use file as test set"
    print " -v, --verbose: turn on verbose mode"
    print " -x file, --cross-validation=file: use file as cross-validation set"
    print " -y file, --cross-validation-output=file: write cross-validation results to file (use with the -x flag)"


if __name__ == '__main__':
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:t:vx:y:", 
                                   ["help", "train", "output", "test", 
                                    "verbose", "cross-validation", 
                                    "cross-validation-output"])
    except getopt.GetoptError, err:
        print str(err)
        help_error_message()
        sys.exit(2)
    
    train_file = None
    test_file = None
    output_file = None
    cross_validation_file = None
    cross_validation_output_file = None
    verbose = False
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-i", "--train"):
            train_file = a
        elif o in ("-o", "--output"):
            output_file = a
        elif o in ("-t", "--test"):
            test_file = a
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-x", "--cross-validation"):
            cross_validation_file = a
        elif o in ("-y", "--cross-validation-output"):
            cross_validation_output_file = a
        else:
            print "Error: unrecognized flag " + o
            help_error_message()
            sys.exit(2)
    
    try:
        assert train_file != None, \
               "Error: training data file must be specified with -i"
        assert not (output_file == None and cross_validation_output_file == None), \
               "Error: an output file must be specified with -o (test) or -y (cross-validation)"
        assert not (test_file != None and output_file == None), \
               "Error: if test file is specified, output file must be specified with -o"
        assert not (output_file != None and test_file == None), \
               "Error: if output file is specified, test file must be specified with -t"
        assert not (cross_validation_file != None and cross_validation_output_file == None), \
               "Error: if cross-validation file is specified, cross-validation output file must be specified with -y"
        assert not (cross_validation_output_file != None and cross_validation_file == None), \
               "Error: if cross-validation output file is specified, cross-validation file must be specified with -x"
    except AssertionError, err:
        print str(err)
        help_error_message()
        sys.exit(2)
    
    # Fill in code below as needed
    #predictor = None
    #predictor.train(train_file)
    if cross_validation_file != None:
        pass
        #predictor.cross_validate(cross_validation_file, cross_validation_output_file)
    if output_file != None:
        pass
        #predictor.predict(test_file, output_file)
