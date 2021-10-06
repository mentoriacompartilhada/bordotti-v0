import pandas as pd
from os import listdir
from os.path import join

class Local_model():
    path = r'C:\Users\carvag14\Documents\Mentoria\compartilhada\bordotti-v0\p0'

    def save(self, rows, columns, filename='local_file.csv'):
        df = pd.DataFrame(rows, columns=columns)
        if filename not in listdir(self.path):
            df.to_csv(join(self.path, filename), sep=';')
        else:
            local = pd.read_csv(join(self.path, filename), sep=';')
            local = local.append(df)
            local.to_csv(join(self.path, filename), sep=';')


    def retrieve(self, id, filename='local_file.csv'):
        local = pd.read_csv(join(self.path, filename), sep=';')
        return local[local['id'] == id].copy()