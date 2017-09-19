import os
from collections import namedtuple
from datetime import datetime


# primary interface to generate named tuple from file. and take a named tuple and convert to a text string for file. 
class MoodManager:    
    def __init__(self, file_default=None):
        self.header_length = None
        self.currently_held_moods = []
        self.file_handler = FileHandler(file_default=file_default)    
    
    def initialize(self):
        if not self.file_handler.is_data_file():
            self.file_handler.create_base_data_file() 
    
    def construct_mood_event_objects(self):
        file_generator = self.file_handler.get_data_file_generator()
        header = self.split_line(file_generator.__next__())
        # in future you can take the header and pass items as arguments for tuple or json/ database entry. 
        self.header_length = len(header)
        for entry_line in file_generator:
            single_entry_list = self.split_line(entry_line)
            self.build_single_mood_event( single_entry_list)
            
    def split_line(self, single_line):
        return single_line.replace('\n', '').split(',')
    
    def build_single_mood_event(self, single_entry_list):
        if len(single_entry_list) == self.header_length:            
            self.append_single_mood_event(MoodEvent( *single_entry_list))   
    
    def append_single_mood_event(self, mood_event):
        self.currently_held_moods.append(mood_event)
           
    # datetime object into "01/11/1986, 0100" format
    def date_to_string_list(self, date_time):
        return date_time.strftime('%m/%d/%Y,%H%M').split(',')
        
    #"01/11/1986, 0100" into datetime object. First taking in both items. 
    def string_pair_to_date(self, text_date, text_time):
        return datetime.strptime('{},{}'.format(text_date, text_time), '%m/%d/%Y,%H%M')
        
    # user event, logging a single mood
    def log_new_mood(self, mood_rating):
        mood_event = self.date_to_string_list(datetime.now())
        mood_event.append(mood_rating)
        self.build_single_mood_event(mood_event)
        self.construct_new_text_line(mood_event)
    
    def construct_new_text_line(self, mood_event):
        
        self.file_handler.append_data_file_entry(','.join(str(item) for item in mood_event))
       
 

# single mood event within tuple. 
class MoodEvent(namedtuple('MoodEvent', 'date time rating')):
    def __new__(cls, date, time, rating):
        return super(MoodEvent, cls).__new__(cls, date, time, rating)
        
    
# primary interface between the text storage and the data manipulation
class FileHandler:    
    def __init__(self, file_default=None):
        self.default = 'events.csv'
        self.default_header = 'date,time,rating\n'
        self.write = 'w'
        self.append = 'a'
        self.new_line = '\n'
        self.file_location = self.file_location(file_default)        
    
    def file_location(self, file_override=None):
        file_name = self.default        
        if file_override:
            file_name = file_override
            
        return self.append_file_base(file_name)
        
    def append_file_base(self, file_name):
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
        
    def is_data_file(self):
        return os.path.isfile(self.file_location)
        
    def create_base_data_file(self):
        self.write_data_file(self.default_header, type=self.write)

    def write_data_file(self, single_line, type=None):
        single_line = self.adjust_new_line(single_line)
        
        with open(self.file_location, type) as data_file:
            data_file.write(single_line)
   
    def adjust_new_line(self, single_line):
        if not self.is_new_line_in(single_line):
            single_line += self.new_line
        return single_line
    
    def is_new_line_in(self, single_line):
        return self.new_line in single_line
        
    def append_data_file_entry(self, single_line):
        self.write_data_file(single_line, self.append)   
    
    # return generator, can cause exception (file was deleted, or file currently being used)
    def get_data_file_generator(self):
        return (single_line for single_line in open(self.file_location, 'r'))    
          
    ### Implement these below if you want ####
    def delete_single_entry(self, entry):
        # maybe delete a value by index, or lne number or something (other than the header at beginning
        return
    
    def delete_all_values(self):
        # allow deletion of the file
        return
            
    def file_exception_handler(self, thrown_exception):
        # trying to open when file is already locked for editing
        # trying to add when file is locked
        # trying to delete when file is locked
        # file currently in use        
        return
        
    # how do you want to implement loading partial files? (graph last few days, variable range).
    def partial_loading(self, lines=None, first_date=None, last_date=None):
        # some way of loading partial results. 
        return
        
    
    
if __name__ == '__main__':  
    mm = MoodManager()
    mm.construct_mood_event_objects()
    # just look at the first 10 for now
    for item in mm.currently_held_moods[:10]:
        print('{} ; {} ; {}'.format(item, 
                        mm.string_pair_to_date(item.date, item.time), 
                        mm.date_to_string_list(mm.string_pair_to_date(item.date, item.time))))
        
    # get current time and constructs the correct namedtuple object, adds to list; also adds string to text file. 
    # mm.log_new_mood(4)
    
    
    