from js import document, localStorage, Object

memos = localStorage

new_memo = Element('new-memo')
add_memo_form = Element('add-memo-form')
memo_container = Element('memo-container')

update_memo = Element('update-memo')
edit_memo_form = Element('edit-memo-form')
edit_memo_container = Element('edit-memo-container')


def add_new_memo(e):
    e.preventDefault()
    localStorage.setItem(get_next_memo_id(), new_memo.element.value)
    new_memo.element.value = ""
    get_memos()

# Returns an integer that is the next memo id


def get_next_memo_id():
    # declares an empty python dictionary
    memo_dict = dict({})
    next_id = 0

    # function to loop through local storage and add all the key-value pairs to the python dictionary
    def memo_loop(memos_entries, _, __):
        memo_dict[memos_entries[0]] = memos_entries[1]

    Object.entries(memos).map(memo_loop)

    # Check for the max id in the dictionary and assign the value to next_id
    for memo_key in memo_dict:
        if next_id < int(memo_key):
            next_id = int(memo_key)

    return next_id + 1

# Function to fetch and append all memos to the document


def get_memos():
    # Clean inside the memo container lelement
    memo_container.element.innerHTML = ""
    # loop through all memo to append them to the memo container
    Object.entries(memos).forEach(memo_entries_loop)


def memo_entries_loop(memo_list, _, __):
    key = str(memo_list[0])
    memo = memos.getItem(key)
    # Creates new list element and buttons for editing and deleting memo
    btn_wrapper = document.createElement("div")
    memo_elem = document.createElement('li')
    memo_edit_btn = document.createElement(
        'button')
    memo_del_btn = document.createElement('button')

    # Set classes and id for element
    btn_wrapper.className = "flex"
    btn_wrapper.id = key
    memo_del_btn.className = "delete-btn"
    memo_edit_btn.className = "edit-btn"
    memo_elem.className = "memo-" + key

    memo_edit_btn.innerText = "Edit"
    memo_del_btn.innerText = "Delete"
    memo_elem.innerText = memo

    # Append buttons to list element
    btn_wrapper.appendChild(memo_edit_btn)
    btn_wrapper.appendChild(memo_del_btn)

    memo_elem.appendChild(btn_wrapper)
    # events
    memo_del_btn.onclick = delete_memo
    memo_edit_btn.onclick = open_edit_container

    # append the new memo to the container
    memo_container.element.appendChild(
        memo_elem)


# Function to delete a memu using the key passed to parent as id
def delete_memo(e):
    memo_id = e.target.parentNode.id
    memos.removeItem(memo_id)
    get_memos()

# Function to edit a memu using the key passed to parent as id


def edit_memo(e):
    e.preventDefault()
    memo_id = e.target.classList
    memos.setItem(memo_id, update_memo.element.value)
    close_edit_container()
    get_memos()

# Function to toggle the edit container


def open_edit_container(e):
    memo_id = e.target.parentNode.id

    edit_memo_container.element.classList.add("open")
    edit_memo_form.element.className = memo_id
    update_memo.element.value = memos.getItem(memo_id)


def close_edit_container():
    edit_memo_form.element.className = ""
    update_memo.element.value = ""
    edit_memo_container.element.classList.remove("open")


get_memos()

# Events
add_memo_form.element.onsubmit = add_new_memo
edit_memo_form.element.onsubmit = edit_memo
