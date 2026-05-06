%====================================================================================
% firefly description   
%====================================================================================
dispatch( cellstate, cellstate(X,Y,COLOR) ).
dispatch( sync_on, sync_on(S) ).
dispatch( sync_off, sync_off(S) ).
event( data, distance(D) ).
%====================================================================================
context(ctxfirefly, "localhost",  "TCP", "8040").
context(ctxgrid, "127.0.0.1",  "TCP", "8050").
 qactor( griddisplay, ctxgrid, "external").
  qactor( sonar, ctxfirefly, "it.unibo.sonar.Sonar").
 static(sonar).
  qactor( sync_actor, ctxfirefly, "it.unibo.sync_actor.Sync_actor").
 static(sync_actor).
  qactor( firefly1, ctxfirefly, "it.unibo.firefly1.Firefly1").
 static(firefly1).
  qactor( firefly2, ctxfirefly, "it.unibo.firefly2.Firefly2").
 static(firefly2).
  qactor( firefly3, ctxfirefly, "it.unibo.firefly3.Firefly3").
 static(firefly3).
  qactor( firefly4, ctxfirefly, "it.unibo.firefly4.Firefly4").
 static(firefly4).
  qactor( firefly5, ctxfirefly, "it.unibo.firefly5.Firefly5").
 static(firefly5).
  qactor( firefly6, ctxfirefly, "it.unibo.firefly6.Firefly6").
 static(firefly6).
