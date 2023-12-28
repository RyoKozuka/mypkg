import launch
import launch.actions
import launch.substitutions
import launch_ros.actionws


def generate_launch_discription():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
            )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener',
            output='screen'
            )
    return launch.LaunchDescription([talker, listener])
