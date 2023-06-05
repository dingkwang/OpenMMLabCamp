# RTMDet result
My ear

<img src="https://github.com/dingkwang/OpenMMLabCamp/blob/main/projects/hw_1_mmpose/myear_detection.png" width="100">

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.819
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.970
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.970
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.819
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.852
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.852
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.852
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.852
06/04 16:19:14 - mmengine - [4m[97mINFO[0m - bbox_mAP_copypaste: 0.819 0.970 0.970 -1.000 -1.000 0.819
06/04 16:19:14 - mmengine - [4m[97mINFO[0m - Epoch(test) [11/11]    coco/bbox_mAP: 0.8190  coco/bbox_mAP_50: 0.9700  coco/bbox_mAP_75: 0.9700  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.8190  data_time: 0.2565  time: 0.4877
```

# RTMPose result
<img src="https://github.com/dingkwang/OpenMMLabCamp/blob/main/projects/hw_1_mmpose/my_ear.gif" width="100">
```
Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.721
Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.942
Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.721
Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.762
Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.952
Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.762
06/04 15:22:27 - mmengine - INFO - Evaluating PCKAccuracy (normalized by ``"bbox_size"``)...
06/04 15:22:27 - mmengine - INFO - Evaluating AUC...
06/04 15:22:27 - mmengine - INFO - Evaluating NME...
06/04 15:22:27 - mmengine - INFO - Epoch(test) [6/6]    coco/AP: 0.721174  coco/AP .5: 1.000000  coco/AP .75: 0.942045  coco/AP (M): -1.000000  coco/AP (L): 0.721174  coco/AR: 0.761905  coco/AR .5: 1.000000  coco/AR .75: 0.952381  coco/AR (M): -1.000000  coco/AR (L): 0.761905  PCK: 0.973923  AUC: 0.109977  NME: 0.043008  data_time: 0.875050  time: 1.275321

```

