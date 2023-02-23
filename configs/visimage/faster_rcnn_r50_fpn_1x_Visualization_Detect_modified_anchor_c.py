#config

# 这个新的配置文件继承自一个原始配置文件，只需要突出必要的修改部分即可
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco_modified_anchor_visualization.py'

# 我们需要对头中的类别数量进行修改来匹配数据集的标注
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=30)))

# 修改数据集相关设置
dataset_type = 'CocoDataset'

classes = ('flow_diagram', 'scatterplot', 'bar_chart', 'graph', 'treemap', 'table', 'line_chart', 'tree', 'small_multiple', 'heatmap', 'matrix', 'map', 'pie_chart', 'sankey_diagram', 'area_chart', 'proportional_area_chart', 'glyph_based', 'stripe_graph', 'parallel_coordinate', 'sunburst_icicle', 'unit_visualization', 'polar_plot', 'error_bar', 'box_plot', 'sector_chart', 'word_cloud', 'donut_chart', 'hierarchical_edge_bundling', 'chord_diagram', 'storyline')

data = dict(
    train=dict(
        img_prefix='./data/Dataset_Visualization_Detect/train/',
        classes=classes,
        ann_file='./data/Dataset_Visualization_Detect/annotations/train_visual_annotations_vis.json'),
    val=dict(
        img_prefix='./data/Dataset_Visualization_Detect/valid/',
        classes=classes,
        ann_file='./data/Dataset_Visualization_Detect/annotations/valid_visual_annotations_vis.json'),
    test=dict(
        img_prefix='./data/Dataset_Visualization_Detect/test/',
        classes=classes,
        ann_file='./data/Dataset_Visualization_Detect/annotations/test_visual_annotations_vis.json'))

# # 我们可以使用预训练的 faster R-CNN 来获取更好的性能
load_from = 'work_dirs/faster_rcnn_r50_fpn_1x_Visualization_Detect_modified_anchor/epoch_12.pth'