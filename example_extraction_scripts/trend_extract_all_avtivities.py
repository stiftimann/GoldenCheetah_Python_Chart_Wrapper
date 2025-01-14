import threading
from datetime import datetime
import os

# Inputs:
# Location for exportet Data:
store_location = "d:/Eigene Dateien/_Stifti/Fahrrad/Berechnungen/GoldenCheeta/Git/GoldenCheetah_Python_Chart_Wrapper/GC_Wrapper/GC_DATA/Tina"
# Number of exportet Acivities beginning from the latest (z_stop = 2000 means all acivities).
z_stop = 5

start = datetime.now()

athlete = GC.athlete()
try:
    athlete_body = GC.seasonMeasures(all=True, group="Body")
    athlete_body_found = True
except SystemError:
    print("No body measurement found create empty file")
    athlete_body_found = False

# Activity List:
activity = GC.activity()
activity_list = sorted(GC.activities( filter='Data contains "P" and Data contains "H"'), reverse = True)

# Activities:
z = 0
for i in activity_list:
    activity = GC.activity(activity=i)
    z += 1
    dt = datetime.strftime(i, "%Y_%m_%d_%H_%M_%S")
    filename = "activity_single_extract_data_" + str(dt) + ".py"
    print('Nr.: ' + str(z) + ' Filename: ' + str(filename))
    f = open(os.path.join(store_location, filename), "w+")
    f.writelines("nan=0 chr(10)+chr(13)")
    f.writelines("activity_data = { chr(10)+chr(13)")
    for key in activity.keys():
        f.writelines("    '" + str(key) + "': " + str(list(activity[key])) + ", chr(10)+chr(13)")
    f.writelines("chr(10)+chr(13) }")
    f.close()	
    if z == z_stop:
        break


def write_activity_list():
    f = open(os.path.join(store_location, "activity_list.py"), "w+")
    f.writelines("import datetimechr(10)+chr(13)")
    f.writelines("activity_list = " + str(activity_list))
    f.close()


if __name__ == "__main__":
    p = [
	threading.Thread(target=write_activity_list, args=()),
    ]

    start = datetime.now()
    for i in p:
        i.start()

    for i in p:
        i.join()

    print('Write data: {}'.format(datetime.now() - start))
