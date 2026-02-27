from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger


@register("MyAstrBot", "BDFFZI", "BDFFZI的AstrBot", "1.0.0")
class MyPlugin(Star):
    # 系统构造函数
    def __init__(self, context: Context):
        super().__init__(context)

    # 插件开始事件
    async def initialize(self):
        pass

    # 插件销毁事件
    async def terminate(self):
        pass

    # 全局信息过滤器
    @filter.event_message_type(filter.EventMessageType.ALL)
    async def on_all_message(self, event: AstrMessageEvent):

        message_chain = event.get_messages()
        logger.info(message_chain)

        event.continue_event()

    # /hello 指令
    @filter.command("hello")
    async def hello(self, event: AstrMessageEvent):
        """这是一个 hello 指令"""  # 指令描述
        user_name = event.get_sender_name()
        yield event.plain_result(f"你好，{user_name}！")
