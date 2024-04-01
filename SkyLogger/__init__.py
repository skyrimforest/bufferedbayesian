
# This Module provides log functionality,
# you can use function there create many
# different log file in directory loginfo.

from .service_log import get_current_time,get_logger
__all__=['get_current_time','get_logger']