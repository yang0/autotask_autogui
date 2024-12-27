from typing import Dict, Any
from autotask.nodes import Node, register_node, ConditionalNode

@register_node
class ConditionNode(ConditionalNode):
    """条件判断节点"""
    NAME = "条件判断"
    DESCRIPTION = "判断输入值是否为真，根据结果执行不同分支"
    CATEGORY = "控制流"
    
    INPUTS = {
        "value": {
            "label": "输入值",
            "description": "要判断的值，非空且非False时执行true分支",
            "type": "ANY",
            "required": True
        }
    }
    
    OUTPUTS = {
        "true_branch": {
            "label": "True分支",
            "description": "条件为真时的输出",
            "type": "ANY"
        },
        "false_branch": {
            "label": "False分支",
            "description": "条件为假时的输出",
            "type": "ANY"
        }
    }

    def execute(self, node_inputs: Dict[str, Any], workflow_logger) -> Dict[str, Any]:
        try:
            value = node_inputs.get("value")
            workflow_logger.debug(f"条件判断输入值: {value}")
            
            # Python的真值判断
            result = bool(value)
            workflow_logger.debug(f"条件判断结果: {result}")

            return {
                "condition_result": result
            }

        except Exception as e:
            error_msg = f"条件判断失败: {str(e)}"
            workflow_logger.error(error_msg)
            return {
                "condition_result": None
            }

    def get_active_branch(self, outputs: Dict[str, Any]) -> str:
        """返回激活的分支名称"""
        return "true_branch" if outputs.get("condition_result") else "false_branch"
