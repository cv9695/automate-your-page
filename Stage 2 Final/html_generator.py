def generate_section_HTML(section_title, information):
    html_text_1 = '''
<div class="section">
    <div class="section-title">
        ''' + section_title
    html_text_2 = '''
    </div>
    <div class="information">
        <p>''' + information + '</p>'
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(section):
    section_title = section[0]
    information = section[1]
    return generate_section_HTML(section_title, information)

EXAMPLE_LIST_OF_SECTIONS = [ ['Structured Data', 'Strings are a sequence of characters and we can operate on sub-sequences of the string. Lists are a sequence of anything. Elements in the lists can be strings, numbers, or other lists. Lists are more powerful than strings.'],
                             ['Mutability', 'The ability to mutate means that we can change the value of a list once we create it, and mutating allows you to change list elements while keeping the same list.'],
                             ['The Difference between Append and "+"', 'Append is a method used with a list to add a new element(s) to an existing list, and does not create a new list. The plus ("+") operator is similar to concatenation with strings, and does not mutate the lists, but combines two lists to create a new list.'] ]


def make_HTML_for_many_sections(list_of_sections):
    HTML = ""
    for section in list_of_sections:
        section_HTML = make_HTML(section)
        HTML = HTML + section_HTML
    return HTML

print make_HTML_for_many_sections(EXAMPLE_LIST_OF_SECTIONS)
