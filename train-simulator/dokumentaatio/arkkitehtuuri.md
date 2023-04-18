```mermaid
classDiagram
 Level -- StaticSprite
 Level -- Train
 Track -- Train
 Track -- TrackRepository


 class Level{
 trains
 tracks
 forests
 stops
 bottlenecks
 all_sprites
 level_map
 display
 _initialize_sprites()
 draw_train()
 
 
 }
 class StaticSprite{
 image
 rect.x
 rext.y
 }
 
 class Track{
 name
 start_xy
 start 
 dest
 stops
 speed_limits
 distances
 bottlenecks
 next_stop()
 speed_to_stop()
 distance_to_stop()
 }
 class Train{
 image
 env
 name
 process
 next_stop
 rect.x
 rext.y
 level
 driving()
 reaching_bottleneck()
 move_train()
  }
 class TrackRepository{
 station_coordinates
 routes
 speedlimits
 distances
 station_xy_coordinates()
 }
 ```
