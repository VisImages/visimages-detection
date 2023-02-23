#config

# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=30)))

# 修改数据集相关设置
dataset_type = 'CocoDataset'

classes = ('flow_diagram', 'scatterplot', 'bar_chart', 'graph', 'treemap', 'table', 'line_chart', 'tree', 'small_multiple', 'heatmap', 'matrix', 'map', 'pie_chart', 'sankey_diagram', 'area_chart', 'proportional_area_chart', 'glyph_based', 'stripe_graph', 'parallel_coordinate', 'sunburst_icicle', 'unit_visualization', 'polar_plot', 'error_bar', 'box_plot', 'sector_chart', 'word_cloud', 'donut_chart', 'hierarchical_edge_bundling', 'chord_diagram', 'storyline')

data = dict(
    train=dict(
        img_prefix='./data/visual_dataSet/train/',
        classes=classes,
        ann_file='./data/visual_dataSet/annotations/train_visual_annotations_vis.json'),
    val=dict(
        img_prefix='./data/visual_dataSet/test/',
        classes=classes,
        ann_file='./data/visual_dataSet/annotations/test_visual_annotations_vis.json'),
    test=dict(
        img_prefix='./data/visual_dataSet/test/',
        classes=classes,
        ann_file='./data/visual_dataSet/annotations/test_visual_annotations_vis.json'))

# # 我们可以使用预训练的 Mask R-CNN 来获取更好的性能
# load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'