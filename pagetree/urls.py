from django.conf.urls.defaults import patterns

urlpatterns = patterns('pagetree.views',
                       (r'^reorder_pageblocks/(?P<id>\d+)/', 'reorder_pageblocks',{},"reorder-pageblocks"),
                       (r'^reorder_section_children/(?P<id>\d+)/','reorder_section_children',{},"reorder-section-children"),
                       (r'^section/add/(?P<section_id>\d+)/$', 'add_childsection', {}, "add-childsection"),
                       (r'^pageblock/add/(?P<section_id>\d+)/$', 'add_pageblock', {}, "add-pageblock"),
                       (r'^pageblock/edit/(?P<block_id>\d+)/$','edit_pageblock',{},"edit-pageblock"),
)
