var kantipur_unicode_obj = {
    q: "त्र",    w: "",    e: "भ",    r: "च",    t: "त",
    y: "थ",    u: "ग",    i: "ष्",    o: "य",    p: "उ",
    a: "ब",    s: "क",    d: "म",    f: "ा",    g: "न",
    h: "ज",    j: "व",    k: "प",    l: "ि",    z: "श",
    x: "ह",    c: "अ",    v: "ख",    b: "द",    n: "ल",
    Q: "त्त",    W: "ध्",    E: "भ्",    R: "च्",
    T: "त्",    Y: "थ्",    U: "ग्",    I: "क्ष्",    O: "इ",
    P: "ए",    A: "ब्",    S: "क्",    D: "म्",    F: "ा",
    G: "न्",    H: "ज्",    J: "व्",    K: "प्",    L: "ी",
    Z: "श्",    X: "ह्",    C: "ऋ",    V: "ख्",    B: "द्य",
    N: "ल्",    M: ":",        1: "ज्ञ",    2: "द्द",
    3: "घ",    4: "द्ध",    5: "छ",    6: "ट",    7: "ठ",
    8: "ड",    9: "ढ",    0: "ण्",    "!": "१",    "@": "२",
    "#": "३",    "$": "४",    "%": "५",    "^": "६",    "&": "७",
    "*": "८",    "(": "९",    ")": "०",    "-": "(",    "_": ")",
    "=": ".",    "+": ".",    "[": "ृ",    "{": "र्",    ";": "स",
    ":": "स्",    "\'": "ु",    "\"": "ू",    "}": "ै",    "]": "े",
    "\\": "्",    "|": "्र",    ",": ",",    "<": "?",    ".": "।",
    ">": "श्र",    "/": "र",    "?": "रु"};

useKantipur = {
    value: false,
    set: function (val) {
	localStorage.setItem('use-kantipur', val);
    },
    get: function () { return localStorage.getItem('use-kantipur'); },
    toggle: function() { this.set(this.get() == "true" ? "false" : "true"); }
};

caretPoint = 0;

function set_toggle_kantipur_value() {
    caretPoint = $('textarea').val().length;
    el = $("#toggle-kantipur");
    if (useKantipur.get() == "true")
	el.html("Disable Kantipur");
    else el.html("Enable Kantipur");

}

function toggle_use_kantipur() {
    caretPoint = $('textarea').val().length;
    useKantipur.toggle();
    set_toggle_kantipur_value();
}

function mapKeys() {
    $('textarea').each(function (index) {
	$(this).on('keydown', function(e){
	    if (!( e.ctrlKey || e.altKey ) && useKantipur.get() == "true"){
		if (kantipur_unicode_obj.hasOwnProperty(e.key)){
		    e.preventDefault();
		    let el = $(this);
		    let caretPos = el[index].selectionStart || 0;
		    let value = el.val();
		    el.val(value.substring(0, caretPos) + kantipur_unicode_obj[e.key] + value.substring(caretPos));
		    el[index].setSelectionRange(caretPos + 1, caretPos + 1);
		}
		else if ( e.key == "m" ) {
		    e.preventDefault();
		    let el = $(this);
		    let caretPos = el[index].selectionStart || 0;
		    let value = el.val();
		    let prev = value[caretPos - 1];
		    let outpur_value = "";
		    switch (prev) {
		    case "र":
			output_value = "रू";
			break;
		    case "उ":
			output_value = "रू";
			break;
		    case "क":
			output_value = "क्र";
			break;
		    case "प":
			output_value = "फ";
			break;
		    case "व":
			output_value = "क";
			break;
		    case "भ":
			output_value = "झ";
			break;
		    default:
			output_value = "";
			break;
		    }
		    console.log(caretPos, value);
		    el.val(value.substring(0, caretPos - prev.length) + output_value + value.substring(caretPos));
		    el[index].setSelectionRange(caretPos + output_value.length - 1, caretPos + output_value.length - 1);
		}
	    }
	});
    });
}

// function mapKeys() {
//     $('textarea').each(function (index) {
// 	$(this).on('keyup', function(e){
// 	    if (useKantipur.get() == "true"){
// 		value = $(this).val();
// 		var parsed = kantipur.parse(value.substring(caretPoint));
// 		$(this).val( value.substring(0, caretPoint) + parsed + value.substring(caretPoint)).focus();
// 		previous_value = value;
// 	    }
// 	});
//     });
// }



$(document).ready(
    function () {
	set_toggle_kantipur_value();
	mapKeys();
    }
);
