# roasbag_timeduiqi.py
import rospy
import rosbag
import sys
import std_msgs

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bag_name = '/home/touchair/bag/GPS_IMU_FIX.bag'
out_bag_name = '/home/touchair/bag/GPS_IMU_SYNC.bag'


with rosbag.Bag(out_bag_name, 'w') as outbag:
    stamp = None
    imu_flag = False
    for topic, msg, t in rosbag.Bag(bag_name).read_messages():
        if topic == '/android/imu':
            imu_flag=True
            t_old = t
            old_stamp=msg.header.stamp

        # elif topic == '/cam0/image_raw':
        #     outbag.write(topic, msg, msg.stamp)
        #     continue
        # print msg.header
        print(topic, msg.header.stamp, t)
        if imu_flag and topic != "/android/imu":

            msg.header.stamp=old_stamp
            outbag.write(topic, msg, t_old)
            # imu_flag=False
        else:
            outbag.write(topic, msg, t)

print("finished")