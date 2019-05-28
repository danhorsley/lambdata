class frame_ops():
        def __init__(self):
            self.dims=0

            
        def make_percent(self,frame,columns,format=False):
            #takes a column and turns each value into the percentage of the total
            #formatting is optional
            #columns can be name or list or you can set columns to 'all'
            if type(columns)==str and columns!='all':
                cols=[columns]
            elif columns=='all':
                cols=frame.columns
            else:
                cols=columns
            for col in cols:
                frame[col]=frame[col]/frame[col].sum()
                if format:
                    frame[col]=pd.Series(["{0:.2f}%".format(val * 100) for val in frame[col]], index = df.index)

        def normalize(self,frame,col):
            #takes a column and normalizes it
            frame[col]=(frame[col]-frame[col].mean())/frame[col].std()