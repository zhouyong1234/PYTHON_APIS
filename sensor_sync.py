#!/usr/bin/env python
# coding=UTF-8
'''
此程序为测试测试程序， 用以测试message_filters同时
订阅两个topic，可以同时进行数据处理。
'''
import rospy, math, random, cv_bridge, cv2
import message_filters
from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu

def multi_callback(subscriber_img, subscriber_imu, subscriber_gps):
    print(type(subscriber_img))
    print("img stamp: ", subscriber_img.header.stamp)
    print("imu stamp: ", subscriber_imu.header.stamp)
    print("gps stamp: ", subscriber_gps.header.stamp)
    print("----------------------------------------")
    img_pub.publish(subscriber_img)
    imu_pub.publish(subscriber_imu)
    gps_pub.publish(subscriber_gps)


if __name__ == '__main__':
    rospy.init_node('sensor_sync', anonymous=True)#初始化节点

    # subscriber_img = message_filters.Subscriber('/image', Image)
    # subscriber_imu = message_filters.Subscriber('/android/imu', Imu)
    # subscriber_gps = message_filters.Subscriber('/android/fix', NavSatFix)


    
    img_pub = rospy.Publisher('/img_sync', Image, queue_size=100)
    imu_pub = rospy.Publisher('/imu_sync', Imu, queue_size=100)
    gps_pub = rospy.Publisher('/gps_sync', NavSatFix, queue_size=100)


    subscriber_img = message_filters.Subscriber('/image', Image)
    subscriber_imu = message_filters.Subscriber('/android/imu', Imu)
    subscriber_gps = message_filters.Subscriber('/android/fix', NavSatFix)
 
    sync = message_filters.ApproximateTimeSynchronizer([subscriber_img, subscriber_imu, subscriber_gps], 10, 0.1)#同步时间戳，具体参数含义需要查看官方文档。
    sync.registerCallback(multi_callback)#执行反馈函数
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("over!")
        cv2.destroyAllWindows()

