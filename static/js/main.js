var AJAX_TIMEOUT = 60000;
var STACK_MAX_LENGTH = 99;

$(document).ready(function () {
	var windowHeight = $(window).height();
	var rows = $("table tr").length;
	var myIconWidth = $(".ui-myicon").width();
	var myIconHeight = windowHeight * 0.865 / rows;
	var myIconMinLen = (myIconHeight > myIconWidth) ? myIconWidth : myIconHeight;
	$(".ui-myicon").css("height", myIconHeight);
	$(".ui-myicon").css("background-size", myIconMinLen * 0.5);

	var stack = new Stack();

	$(".ui-myicon").touchstart(function () {
		if (stack.size() >= STACK_MAX_LENGTH) {
			return;
		}
		var direction = $(this).children("input:hidden[name='direction']").first().attr("value");
		var speed = $(".ui-myrange input").first().val();
		stack.push(new stack.Node(direction, speed));
		$.ajax({
			type: "post",
			dataType: "json",
			url: "/go",
			timeout: AJAX_TIMEOUT,
			data: {
	        	"direction": direction,
	        	"speed": speed,
	        	"stack": stack.print()
			},
			beforeSend: function(XMLHttpRequest) {},
			success: function(data, textStatus) {},
			complete: function(XMLHttpRequest, textStatus) {},
			error: function() {}
		});
	});

	$(".ui-myicon").touchend(function () {
		var direction = $(this).children("input:hidden[name='direction']").first().attr("value");
		var speed = $(".ui-myrange input").first().val();
		var node = stack.pop(new stack.Node(direction, speed));
		if (node == null) {
			if (stack.size() > 0) {
				// 元素不在栈中
				return;
			} else {
				// 栈已空
				node = new stack.Node("reset", 0);
			}
		}
		$.ajax({
			type: "post",
			dataType: "json",
			url: "/go",
			timeout: AJAX_TIMEOUT,
			data: {
	        	"direction": node.direction,
	        	"speed": node.speed,
	        	"stack": stack.print()
			},
			beforeSend: function(XMLHttpRequest) {},
			success: function(data, textStatus) {},
			complete: function(XMLHttpRequest, textStatus) {},
			error: function() {}
		});
	});

});

function Stack() {

	var length = 0;
	var head = null;

	this.Node = function (direction, speed) {
		this.direction = direction;
		this.speed = speed;
		this.next = null;
		this.equals = function (other) {
			return this.direction == other.direction
					&& this.speed == other.speed;
		};
	};

	this.push = function (node) {
		// 空栈
		if (head == null) {
			head = node;
		} else {
			// 非空栈，元素已存在
			var current = head;
			while (current != null) {
				if (current.equals(node)) {
					return;
				}
				current = current.next;
			}
			// 非空栈，元素不存在
			var origin = head;
			node.next = origin;
			head = node;
		}
		length++;
	};

	this.pop = function (node) {
		if (this.length < 2) {
			// 栈中有1个或0个元素
			length = 0;
			head = null;
			return head;
		}
		if (node.equals(head)) {
			// 栈首元素，出栈
			var current = head.next;
			head.next = null;
			head = current;
			length--;
			return current;
		} else {
			// 非栈首元素，遍历查找
			var last = head;
			var current = head;
			while (current != null) {
				if (node.equals(current)) {
					// 找到后出栈
					last.next = current.next;
					length--;
					return head;
				} else {
					last = current;
					current = current.next;
				}
			}
		}
		return null;
	};

	this.size = function () {
		return length;
	};

	this.print = function () {
		if (length == 0) {
			return "-";
		}
		var str = "";
		var current = head;
		while (current != null) {
			str = str + "\"" + current.direction + "\":\"" + current.speed + "\"";
			if (current.next != null) {
				str += ", ";
			}
			current = current.next;
		}
		return str;
	};

}
