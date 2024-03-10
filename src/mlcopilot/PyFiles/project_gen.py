import configs as cf
import os
from datetime import datetime

class Create_Project:

    def __init__(self, logger_object):
        self.logger_object = logger_object

    def generate_project_id(self):
        self.date = datetime.now().date()
        self.time = datetime.now().time()

        self.date_str = str(self.date).replace('-', '')

        self.time_str = str(self.time).replace(':', '').partition('.')[0]

        self.project_id = self.date_str + self.time_str

        return self.project_id
    
    def create_folder_tree(self, project_id):
        self.project_id = project_id
        self.project_folder = os.path.join(cf.FILE_PATH, cf.output_files, self.project_id)
        self.logs_folder = os.path.join(cf.FILE_PATH, cf.output_files, self.project_id, 'Logs')
        self.output_data = os.path.join(cf.FILE_PATH, cf.output_files, self.project_id, 'Output Files')
        [os.mkdir(i) for i in [self.project_folder, self.logs_folder, self.output_data]]
        
    def generate_log(self, project_id):
        self.project_id = project_id
        self.log_file_path = os.path.join(cf.FILE_PATH, cf.output_files, self.project_id, 'Logs', 'Global_Logs.txt')
        self.file_object = open(self.log_file_path, "w")
        self.logger_object.log(self.file_object, f"Entered the generate_log_file method of Create_Project class, project : {self.project_id} created successfully")
        self.file_object.close()

    def initiate_project(self):

        self.project_id = self.generate_project_id()
        self.create_folder_tree(self.project_id)
        self.generate_log(self.project_id)

        return self.project_id
        