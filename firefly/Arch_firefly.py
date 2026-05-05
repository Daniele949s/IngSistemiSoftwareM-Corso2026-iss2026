### conda install diagrams
from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
import os
os.environ['PATH'] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

graphattr = {     #https://www.graphviz.org/doc/info/attrs.html
    'fontsize': '22',
}

nodeattr = {   
    'fontsize': '22',
    'bgcolor': 'lightyellow'
}

eventedgeattr = {
    'color': 'red',
    'style': 'dotted'
}
evattr = {
    'color': 'darkgreen',
    'style': 'dotted'
}
with Diagram('fireflyArch', show=False, outformat='png', graph_attr=graphattr) as diag:
  with Cluster('env'):
     sys = Custom('','./qakicons/system.png')
### see https://renenyffenegger.ch/notes/tools/Graphviz/attributes/label/HTML-like/index
     with Cluster('ctxfirefly', graph_attr=nodeattr):
          sonar=Custom('sonar','./qakicons/symActorWithobjSmall.png')
          sync_actor=Custom('sync_actor','./qakicons/symActorWithobjSmall.png')
          firefly1=Custom('firefly1','./qakicons/symActorWithobjSmall.png')
          firefly2=Custom('firefly2','./qakicons/symActorWithobjSmall.png')
          firefly3=Custom('firefly3','./qakicons/symActorWithobjSmall.png')
     with Cluster('ctxgrid', graph_attr=nodeattr):
          griddisplay=Custom('griddisplay(ext)','./qakicons/externalQActor.png')
     sonar >> Edge( label='data', **eventedgeattr, decorate='true', fontcolor='red') >> sys
     sys >> Edge( label='data', **evattr, decorate='true', fontcolor='darkgreen') >> sync_actor
     sync_actor >> Edge(color='blue', style='solid',  decorate='true', label='<sync_on &nbsp; sync_off &nbsp; >',  fontcolor='blue') >> firefly1
     firefly2 >> Edge(color='blue', style='solid',  decorate='true', label='<cellstate &nbsp; >',  fontcolor='blue') >> griddisplay
     firefly1 >> Edge(color='blue', style='solid',  decorate='true', label='<cellstate &nbsp; >',  fontcolor='blue') >> griddisplay
     sync_actor >> Edge(color='blue', style='solid',  decorate='true', label='<sync_on &nbsp; sync_off &nbsp; >',  fontcolor='blue') >> firefly3
     firefly3 >> Edge(color='blue', style='solid',  decorate='true', label='<cellstate &nbsp; >',  fontcolor='blue') >> griddisplay
     sync_actor >> Edge(color='blue', style='solid',  decorate='true', label='<sync_on &nbsp; sync_off &nbsp; >',  fontcolor='blue') >> firefly2
diag
