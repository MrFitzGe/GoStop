import numpy as np
import pandas as pd

cards = pd.DataFrame(
        {
            "Number": np.array(range(0,48))
            "Month": pd.Categorical(["Jan", "Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar", "Mar", "Apr", "Apr", "Apr", "Apr", "May", "May", "May", "May", "Jun", "Jun", "Jun", "Jun", "Jul", "Jul", "Jul", "Jul", "Aug", "Aug", "Aug", "Aug", "Sep", "Sep", "Sep", "Sep", "Oct", "Oct", "Oct", "Oct", "Nov", "Nov", "Nov", "Nov", "Dec", "Dec", "Dec", "Dec"]) 
            "Group": pd.Categorical(["bright", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "animal", "junk", "junk", "junk", "ribbon", "junk", "junk", "animal", "ribbon", "junk", "junk", "bright", "junk", "junk", "junk", "bright", "animal", "ribbon", "junk"])
            "Special": pd.Categorical(["None", "Red_Writing", "None", "None", "Bird", "Red_Writing", "None", "None", "None", "Red_Writing", "None", "None", "Bird", "Red_Blank", "None", "None", "Maybe_DoubleJunk", "Red_Blank", "None", "None", "None", "Blue_Writing", "None", "None", "None", "Red_Blank", "None", "None", "None", "Bird", "None", "None", "DoubleJunk", "Blue_Writing", "None", "None", "None", "Blue_Writing", "None", "None", "None", "DoubleJunk", "None", "None", "SadMan", "DeadBird", "DeadRibbon", "DoubleJunk"]) 

        }
)
