/* description: Parses and executes mathematical expressions. */

/* lexical grammar */

%lex
%%
"/m"     return "RU_TOKEN"			  /*रू*/
"jm"     return "KA_TOKEN"			  /*क*/
"km"     return "PHA_TOKEN"			  /*फ*/
"em"     return "JHA_TOKEN"			  /*झ*/
"qm"     return "KRA_TOKEN"			  /*क्र*/
"pm"     return "U_TOKEN"			  /*ऊ*/
[^m] return "TOKEN"
<<EOF>>               return "EOF"
/lex
%{
function kantipur_unicode(t) {
	var kantipur_unicode_obj = {
							q: "त्र",
							w: "",
							e: "भ",
							r: "च",
							t: "त",
							y: "थ",
							u: "ग",
							i: "ष्",
							o: "य",
							p: "उ",
							a: "ब",
							s: "क",
							d: "म",
							f: "ा",
							g: "न",
							h: "ज",
							j: "व",
							k: "प",
							l: "ि",
							z: "श",
							x: "ह",
							c: "अ",
							v: "ख",
							b: "द",
							n: "ल",
							1: "ज्ञ",
							2: "द्द",
							3: "घ",
							4: "द्ध",
							5: "छ",
							6: "ट",
							7: "ठ",
							8: "ड",
							9: "ढ",
							0: "ण्",
							"!": "१",
							"@": "२",
							"#": "३",
							"$": "४",
							"%": "५",
							"^": "६",
							"&": "७",
							"*": "८",
							"(": "९",
							")": "०",
							"-": "(",
							"_": ")",
							"=": ".",
							"+": ".",
							"[": "ृ",
							"{": "र्",
							";": "स",
							":": "स्",
							"\'": "ु",
							"\"": "ू",
							"}": "ै",
							"]": "े",
							"\\": "्",
							"|": "्र",
							",": ",",
							"<": "?",
							".": "।",
							">": "श्र",
							"/": "र",
							"?": "रु"
	};
    console.log(t);
    if (kantipur_unicode_obj.hasOwnProperty(t))
        return kantipur_unicode_obj[t];
    return t;
}

%}

/* operator associations and precedence */

%left RU_TOKEN KA_TOKEN PHA_TOKEN JHA_TOKEN KA_TOKEN U_TOKEN

%start expressions

%% /* language grammar */

expressions
    : e EOF
        { return $1; }
    ;

e:				token { $$ = $1; }
		|		token e { $$ = $1 + $2; }
		;

token:			RU_TOKEN      { $$ = "रू" }
		|		KA_TOKEN      { $$ = "क" }
		|		PHA_TOKEN     { $$ = "फ" }
		|		JHA_TOKEN     { $$ = "झ" }
		|		KRA_TOKEN     { $$ = "क्र" }
		|		U_TOKEN       { $$ = "ऊ" }
		|		TOKEN         { $$ = kantipur_unicode($1); }
		;
