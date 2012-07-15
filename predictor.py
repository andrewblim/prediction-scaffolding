
class Predictor:
    
    def __init__(self):
        self.data = {}
    
    def train(self, train_file, verbose=False):
        """
        Train the Predictor on data in train_file. Fill with project-specific
        code as needed. 
        """
        f = open(train_file, 'r')
        f.close()
    
    def cross_validate(self, cross_validation_file, cross_validation_output_file,
                       verbose=False):
        """
        Run cross-validation on the data in cross_validation_file, which should 
        contain a complete set of data in the same format as the training set. 
        Outputs line-by-line performance to cross_validation_output_file. Fill
        with project-specific code as needed. 
        """
        f = open(cross_validation_file, 'r')
        f.close()
        f.open(cross_validation_output_file, 'w')
        f.close()
    
    def predict(self, test_file, output_file, verbose=True):
        """
        Predict based on the test data in test_file, which presumably does not
        contain the values that you need to predict, unlike cross-validation. 
        Outputs the predicted data to output_file. Fill with project-specific
        code as needed. 
        """
        f = open(test_file, 'r')
        f.close()
        f = open(output_file, 'w')
        f.close()
        