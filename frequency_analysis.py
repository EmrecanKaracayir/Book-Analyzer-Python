import re
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

# Variables #
using_database: bool = False  # This determines which method will be used to obtain the book(s). Default value is False
selected_mode = 0  # This variable sets the game mode. (Values can only be '1' or '2')
selected_books: list = []  # This is the book(s) list that user decided on. (It can contain one or two elements)

english_stop_words = {'yourselves', 'because', 'a', 'hadn', 'won', 'am', 'some', 'theirs', 'those', 'them',
                      'how', 'he', "mustn't", 'why', 'needn', 'couldn', 'mightn', 'more', 'didn', 'has',
                      'same', 'itself', 've', 'she', 'this', 'up', "isn't", "aren't", "you've", 'no',
                      'ourselves', "hasn't", 'yours', 'or', 'wouldn', 'where', 's', 'my', 'being', 'me',
                      'their', 'd', 'each', 'by', 'if', 'of', 'than', "weren't", 'above', 'over', "hadn't",
                      'ain', 'now', 'is', 'mustn', "won't", 'own', 'off', 'below', 'shan', 'm', "you'd", 'so',
                      'between', "shan't", "mightn't", 'they', "you're", "it's", 'but', 'few', 'will', 'nor',
                      'did', "shouldn't", 'against', 'be', 'do', 'themselves', 't', "couldn't", "didn't", 'at',
                      'during', 'hers', 'to', 'down', 'weren', 'it', 'into', 'out', 'all', 'doing', 'only',
                      'does', "wouldn't", 'an', 'while', 'had', "you'll", "needn't", "should've", 'the',
                      'most', 'both', 'her', 'been', 'before', 'don', 'ma', 'through', 'and', 'for', 'other',
                      'should', "she's", 'o', 'y', 'haven', 'that', 'i', 'from', 'whom', 'shouldn', 'himself',
                      'once', 'him', 'there', 'about', 'doesn', "doesn't", 'our', 'further', "that'll",
                      'having', 'can', 'which', 'we', "haven't", 'as', 'what', 'again', 'hasn', 'you',
                      'when', 'in', 'after', 'not', 'aren', 'here', 'until', 'too', 'your', 'was', 'very',
                      'ours', 'are', 'under', 're', 'isn', 'yourself', 'such', "wasn't", 'on', 'herself',
                      'were', 'just', 'who', 'these', 'with', 'then', 'myself', 'its', 'll', 'his', 'have',
                      'wasn', "don't", 'any'}  # This is the latest stopwords list from the official NLTK


# Welcome Screen Method #
def welcome_screen():
    print("\n> ### Welcome to E-Book Word Frequency Analysis Tool ###\n")


# Asking The User if He/She Knows Already Which Book He/She Will Select #
def ask_if_the_user_knows_the_books_already():
    # Global Variables #
    global using_database

    # Local Variables #
    user_method_input: str  # This variable declares the game mode. (Values can only be 'Y' or 'N')
    true_input: bool = False

    print("- We provide dynamic database collection from the source.\n"
          "\n> If you want to collect the database from the source and list all the available books:\n"
          "- Please enter 'Y' (It may take 1-2 minutes)\n"
          "\n> If you already know which book(s) to chose:\n"
          "- Please enter 'N'\n")

    # Input Check #
    user_method_input = input("< Input: ")
    while not true_input:
        if user_method_input.upper() == "Y" or user_method_input.upper() == "N":
            true_input = True
        else:
            user_method_input = input("< Input ('Y' or 'N'): ")
            true_input = False
    # Setting The Method Mode #
    if user_method_input.upper() == 'Y':
        using_database = True
        print("\n+ You will be using WFAT Database Collection method.")
    else:
        using_database = False
        print("\n+ You will be using WFAT Direct Input Collection method.")


# Getting Mode Input From User Method #
def get_mode_input():
    # Global Variables #
    global selected_mode

    # Local Variables #
    user_mode_input: str  # This variable declares the game mode. (Values can only be 'Y' or 'N')
    true_input: bool = False

    # Input Check #
    user_mode_input = input("< Input: ")
    while not true_input:
        if user_mode_input.upper() == "Y" or user_mode_input.upper() == "N":
            true_input = True
        else:
            user_mode_input = input("< Input ('Y' or 'N'): ")
            true_input = False
    # Setting The Selected Mode #
    if user_mode_input.upper() == 'Y':
        selected_mode = 2
        print("\n+ You are analysing word frequencies for two books\n")
    else:
        selected_mode = 1
        print("\n+ You are analysing word frequencies for one book\n")


# Scrapes Wikibooks for Book List From Database #
def web_scraping_and_selection_from_database():
    # Global Variables #
    global selected_mode

    # Variables #
    book_count = 0
    all_finished_books_list = []
    progress_bar_indicator = 0

    finished_books_numbers_list = []  # [ book_name, book_link ]
    finished_books_a_list = []  # [ book_name, book_link ]
    finished_books_b_list = []  # [ book_name, book_link ]
    finished_books_c_list = []  # [ book_name, book_link ]
    finished_books_d_list = []  # [ book_name, book_link ]
    finished_books_e_list = []  # [ book_name, book_link ]
    finished_books_f_list = []  # [ book_name, book_link ]
    finished_books_g_list = []  # [ book_name, book_link ]
    finished_books_h_list = []  # [ book_name, book_link ]
    finished_books_i_list = []  # [ book_name, book_link ]
    finished_books_j_list = []  # [ book_name, book_link ]
    finished_books_k_list = []  # [ book_name, book_link ]
    finished_books_l_list = []  # [ book_name, book_link ]
    finished_books_m_list = []  # [ book_name, book_link ]
    finished_books_n_list = []  # [ book_name, book_link ]
    finished_books_o_list = []  # [ book_name, book_link ]
    finished_books_p_list = []  # [ book_name, book_link ]
    finished_books_q_list = []  # [ book_name, book_link ]
    finished_books_r_list = []  # [ book_name, book_link ]
    finished_books_s_list = []  # [ book_name, book_link ]
    finished_books_t_list = []  # [ book_name, book_link ]
    finished_books_u_list = []  # [ book_name, book_link ]
    finished_books_v_list = []  # [ book_name, book_link ]
    finished_books_w_list = []  # [ book_name, book_link ]
    finished_books_x_list = []  # [ book_name, book_link ]
    finished_books_y_list = []  # [ book_name, book_link ]
    finished_books_z_list = []  # [ book_name, book_link ]

    category_items = ["0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # PROGRESS BAR INDICATORS #
    print("\n- The database for books is provided by Wikibooks.")
    print("- Please wait while we search for completed and downloadable books from the database.\n")

    print("> |" + 27 * "-" + "|" +
          "  " + "0" + "%" + "     "
          + "0" + " books found", end="")

    increment = 100 / 27
    current_percent = 0

    for category_item in category_items:
        progress_bar_indicator += 1

        finished_books_object_category = urllib.request.urlopen(
            "https://en.wikibooks.org/w/index.php?title=Category:Completed_books&from=" + category_item.upper())

        finished_books_bytes_category = finished_books_object_category.read()

        finished_books_category_str = finished_books_bytes_category.decode("utf-8")

        finished_books_category_str = str.replace(finished_books_category_str, "\n", "")

        if category_item == "0":
            regex = r'<div class="mw-category-group"><h3>\d<\/h3>(.*?)(?:<\/div>)'
        else:
            regex = r'<div class="mw-category-group"><h3>' + category_item.upper() + r'<\/h3>(.*?)(?:<\/div>)'

        finished_books_category_raw = re.search(regex, finished_books_category_str)

        if finished_books_category_raw is None:
            regex = r'<h3>' + category_item.upper() + r'<\/h3>(.*?)(?:<\/ul>)'
            finished_books_category_raw = re.search(regex, finished_books_category_str)
            finished_books_category_raw_str = '<h3>' + category_item.upper() + '</h3>' \
                                              + finished_books_category_raw.group(1)
        else:
            finished_books_category_raw_str = finished_books_category_raw.group(1)

        regex02 = r'<li>(.*?)(?:<\/li>)'
        finished_books_category_list_raw = re.findall(regex02, finished_books_category_raw_str)

        book_id_number_counter = 0
        for book in finished_books_category_list_raw:
            regex03 = r'title="(.*?)(?:")'
            book_name = re.search(regex03, book)
            book_name_str: str = book_name.group(1)
            if book_name_str.__contains__("&#039;"):
                book_name_str = book_name_str.replace("&#039;", "'")

            regex04 = r'<a href="(.*?)(?:")'
            book_link = re.search(regex04, book)
            book_link_str: str = book_link.group(1)

            if book_id_number_counter < 10:
                book_id_number_counter_str = "00" + book_id_number_counter.__str__()
            elif 100 > book_id_number_counter >= 10:
                book_id_number_counter_str = "0" + book_id_number_counter.__str__()
            else:
                book_id_number_counter_str = book_id_number_counter.__str__()

            if category_item == "0":
                book_id_number_str: str = "NUM" + book_id_number_counter_str
            else:
                book_id_number_str: str = category_item.__str__().upper() + book_id_number_counter_str

            book_properties: list = ["book_name", "book_link", "book_idNumber"]
            book_properties[0] = book_name_str
            book_properties[1] = book_link_str
            book_properties[2] = book_id_number_str

            book_properties[1] = book_properties[1].replace("&#039;", "%27")

            # Checking if the book has a printable version #
            check_if_downloadable_object_book = urllib.request.urlopen(
                "https://en.wikibooks.org" + book_properties[1])

            check_if_downloadable_book = check_if_downloadable_object_book.read()

            check_if_downloadable_book_str = check_if_downloadable_book.decode("utf-8")

            check_if_downloadable_book_str = str.replace(check_if_downloadable_book_str, "\n", "")

            downloadable = check_if_downloadable_book_str.__contains__(book_link_str + "/Print_version")

            if downloadable:
                book_count += 1
                book_id_number_counter += 1

                if category_item == "0":
                    finished_books_numbers_list.append(book_properties)
                elif category_item == "a":
                    finished_books_a_list.append(book_properties)
                elif category_item == "b":
                    finished_books_b_list.append(book_properties)
                elif category_item == "c":
                    finished_books_c_list.append(book_properties)
                elif category_item == "d":
                    finished_books_d_list.append(book_properties)
                elif category_item == "e":
                    finished_books_e_list.append(book_properties)
                elif category_item == "f":
                    finished_books_f_list.append(book_properties)
                elif category_item == "g":
                    finished_books_g_list.append(book_properties)
                elif category_item == "h":
                    finished_books_h_list.append(book_properties)
                elif category_item == "i":
                    finished_books_i_list.append(book_properties)
                elif category_item == "j":
                    finished_books_j_list.append(book_properties)
                elif category_item == "k":
                    finished_books_k_list.append(book_properties)
                elif category_item == "l":
                    finished_books_l_list.append(book_properties)
                elif category_item == "m":
                    finished_books_m_list.append(book_properties)
                elif category_item == "n":
                    finished_books_n_list.append(book_properties)
                elif category_item == "o":
                    finished_books_o_list.append(book_properties)
                elif category_item == "p":
                    finished_books_p_list.append(book_properties)
                elif category_item == "q":
                    finished_books_q_list.append(book_properties)
                elif category_item == "r":
                    finished_books_r_list.append(book_properties)
                elif category_item == "s":
                    finished_books_s_list.append(book_properties)
                elif category_item == "t":
                    finished_books_t_list.append(book_properties)
                elif category_item == "u":
                    finished_books_u_list.append(book_properties)
                elif category_item == "v":
                    finished_books_v_list.append(book_properties)
                elif category_item == "w":
                    finished_books_w_list.append(book_properties)
                elif category_item == "x":
                    finished_books_x_list.append(book_properties)
                elif category_item == "y":
                    finished_books_y_list.append(book_properties)
                else:
                    finished_books_z_list.append(book_properties)

        # PROGRESS BAR #
        if category_item == "0" or category_item == "a":
            blank = "  "
        elif category_item == "z":
            blank = ""
        else:
            blank = " "

        for b in range(0, 80):
            print("\b", end="")

        current_percent += increment
        print("> |" + progress_bar_indicator * "#" + (26 - progress_bar_indicator) * "-"
              + "|" + "  " + current_percent.__int__().__str__() + "%" + "   " + blank
              + book_count.__str__() + " books found", end="")

    # Copying books to all books list #
    all_finished_books_list.append(finished_books_numbers_list)
    all_finished_books_list.append(finished_books_a_list)
    all_finished_books_list.append(finished_books_b_list)
    all_finished_books_list.append(finished_books_c_list)
    all_finished_books_list.append(finished_books_d_list)
    all_finished_books_list.append(finished_books_e_list)
    all_finished_books_list.append(finished_books_f_list)
    all_finished_books_list.append(finished_books_g_list)
    all_finished_books_list.append(finished_books_h_list)
    all_finished_books_list.append(finished_books_i_list)
    all_finished_books_list.append(finished_books_j_list)
    all_finished_books_list.append(finished_books_k_list)
    all_finished_books_list.append(finished_books_l_list)
    all_finished_books_list.append(finished_books_m_list)
    all_finished_books_list.append(finished_books_n_list)
    all_finished_books_list.append(finished_books_o_list)
    all_finished_books_list.append(finished_books_p_list)
    all_finished_books_list.append(finished_books_q_list)
    all_finished_books_list.append(finished_books_r_list)
    all_finished_books_list.append(finished_books_s_list)
    all_finished_books_list.append(finished_books_t_list)
    all_finished_books_list.append(finished_books_u_list)
    all_finished_books_list.append(finished_books_v_list)
    all_finished_books_list.append(finished_books_w_list)
    all_finished_books_list.append(finished_books_x_list)
    all_finished_books_list.append(finished_books_y_list)
    all_finished_books_list.append(finished_books_z_list)

    print("\n\n+ The database has been downloaded.")
    print("\n> To analyse two books to analyse:")
    print("- Please enter 'Y'")
    print("\n> To analyse only one book:")
    print("- Please enter 'N'\n")
    get_mode_input()

    print("- In order to select the book(s) you need to use WFAT commands")
    print("> If you need help with WFAT commands, enter '/help' to get command manual.")

    # COMMAND LOOP #
    loop_ended = False
    selected_list = []

    left_selections: int = selected_mode

    while not loop_ended:
        command: str = input("\n< Command: ")
        if command.split(" ").__len__() > 1:
            main_command = command.split(" ")[0]
            second_command = command.replace(main_command + " ", "")
        else:
            main_command = command
            second_command = None

        if command == "/help":
            print("\n#############################################################################################\n"
                  "|                                    WFAT COMMAND MANUAL                                    |\n"
                  "|       WFAT (Word Frequency Analysis Tool) commands are the dedicated way to control       |\n"
                  "|        this software. You can list, select and analyse the books with the commands.       |\n"
                  "|                         All commands start with the backslash '/'                         |\n"
                  "|                                                                                           |\n"
                  "|                                   ### COMMANDS LIST ###                                   |\n"
                  "|   |--------------------------ACTION-------------------------| |--------COMMAND--------|   |\n"
                  "|                                                                                           |\n"
                  "|   1. '/help' command variations:                                                          |\n"
                  "|   - To read the manual of WFAT commands:                       /help                      |\n"
                  "|                                                                                           |\n"
                  "|   2. '/list' command variations (If you haven't already decided your book(s).):           |\n"
                  "|   - To list all books:                                         /list all                  |\n"
                  "|   - To list the books that starts with numbers:                /list category_num         |\n"
                  "|   - To list the books that starts with 'A':                    /list category_a           |\n"
                  "|   - To list the books that starts with 'B':                    /list category_b           |\n"
                  "|   - ...                                                                                   |\n"
                  "|   - ..                                                                                    |\n"
                  "|   - .                                                                                     |\n"
                  "|                                                                                           |\n"
                  "|   3. '/select' command variations (Listed books will have identity numbers 'idNumber'):   |\n"
                  "|   - To select the book with its identity number:               /select_id idNumber        |\n"
                  "|   - To select the book with its name:                          /select_name bookName      |\n"
                  "|                                                                                           |\n"
                  "|   4. '/reselect' command variations:                                                      |\n"
                  "|   - To reselect the book 1 that you have selected:             /reselect 1                |\n"
                  "|   - To reselect the book 2 that you have selected:             /reselect 2                |\n"
                  "|                                                                                           |\n"
                  "|   5. '/change_mod' command variations (This will reset the current selected book(s):      |\n"
                  "|   - To change the current mode to single book analysis:        /change_mode 1             |\n"
                  "|   - To change the current mode to multiple book analysis:      /change_mode 2             |\n"
                  "|                                                                                           |\n"
                  "|   6. '/analyse' command variations:                                                       |\n"
                  "|   - To start analysing the book(s) you have selected:          /analyse                   |\n"
                  "|                                                                                           |\n"
                  "|   7. '/restart' command variations:                                                       |\n"
                  "|   - To enable loop for WFAT:                                   /restart true              |\n"
                  "|   - To disable loop for WFAT:                                  /restart false             |\n"
                  "|                                                                                           |\n"
                  "#############################################################################################"
                  )
        elif main_command == "/list":
            # Variables #
            wrong_command = False

            if second_command == "category_num":
                selected_list = finished_books_numbers_list
            elif second_command == "category_a":
                selected_list = finished_books_a_list
            elif second_command == "category_b":
                selected_list = finished_books_b_list
            elif second_command == "category_c":
                selected_list = finished_books_c_list
            elif second_command == "category_d":
                selected_list = finished_books_d_list
            elif second_command == "category_e":
                selected_list = finished_books_e_list
            elif second_command == "category_f":
                selected_list = finished_books_f_list
            elif second_command == "category_g":
                selected_list = finished_books_g_list
            elif second_command == "category_h":
                selected_list = finished_books_h_list
            elif second_command == "category_i":
                selected_list = finished_books_i_list
            elif second_command == "category_j":
                selected_list = finished_books_j_list
            elif second_command == "category_k":
                selected_list = finished_books_k_list
            elif second_command == "category_l":
                selected_list = finished_books_l_list
            elif second_command == "category_m":
                selected_list = finished_books_m_list
            elif second_command == "category_n":
                selected_list = finished_books_n_list
            elif second_command == "category_o":
                selected_list = finished_books_o_list
            elif second_command == "category_p":
                selected_list = finished_books_p_list
            elif second_command == "category_q":
                selected_list = finished_books_q_list
            elif second_command == "category_r":
                selected_list = finished_books_r_list
            elif second_command == "category_s":
                selected_list = finished_books_s_list
            elif second_command == "category_t":
                selected_list = finished_books_t_list
            elif second_command == "category_u":
                selected_list = finished_books_u_list
            elif second_command == "category_v":
                selected_list = finished_books_v_list
            elif second_command == "category_w":
                selected_list = finished_books_w_list
            elif second_command == "category_x":
                selected_list = finished_books_x_list
            elif second_command == "category_y":
                selected_list = finished_books_y_list
            elif second_command == "category_z":
                selected_list = finished_books_z_list
            elif second_command == "all":
                selected_list = all_finished_books_list
            else:
                wrong_command = True
                print("\n- Wrong category command entered.\n"
                      "> If you want to learn more about commands, write '/help' without the apostrophes.")

            if selected_list.__len__() != 0 and wrong_command is False:
                print("\n            BOOK LIST")
                print("   idNumber         bookName")
                if second_command != "all":
                    for book in selected_list:
                        if book[2].__str__().__contains__("NUM"):
                            print("- ", book[2], "         ", book[0])
                        else:
                            print("- ", book[2], "           ", book[0])
                elif second_command == "all":
                    for category in selected_list:
                        for book in category:
                            if book[2].__str__().__contains__("NUM"):
                                print("- ", book[2], "         ", book[0])
                            else:
                                print("- ", book[2], "           ", book[0])
            elif selected_list.__len__() == 0 and wrong_command is False:
                print("\n- No books available in the database for this category. Try another one.")
        elif main_command == "/select_id":
            if selected_list.__len__() == 0:
                print("\n> In order to select book(s) with their idNumber, you must list them first!")
            else:
                starting_element_count = selected_books.__len__()
                first_not_empty_item = 0
                for item in selected_list:
                    if item.__len__() != 0:
                        break
                    first_not_empty_item += 1
                if not isinstance(selected_list[first_not_empty_item][0], list):
                    for book in selected_list:
                        if book[2] == second_command.upper():
                            if selected_books.__contains__(""):
                                first_index_of_empty_book = selected_books.index("")
                                selected_books.insert(first_index_of_empty_book, book)
                            else:
                                selected_books.append(book)
                            left_selections -= 1
                            print("\n+ You have selected", '"' + book[0].__str__() + '"', "as your",
                                  (selected_books.index(book) + 1).__str__() + ". book.")
                            break
                else:
                    for category in selected_list:
                        for book in category:
                            if book[2] == second_command.upper():
                                if selected_books.__contains__(""):
                                    first_index_of_empty_book = selected_books.index("")
                                    selected_books.insert(first_index_of_empty_book, book)
                                else:
                                    selected_books.append(book)
                                left_selections -= 1
                                print("\n+ You have selected", '"' + book[0] + '"', "as your",
                                      (selected_books.index(book) + 1).__str__() + ". book.")
                                break
                if selected_books.__len__() == starting_element_count:
                    print("\n- We couldn't find any match in your list for the given idNumber.")
                    print("> Check the current list or the idNumber you write then try again.")
        elif main_command == "/select_name":
            starting_element_count = selected_books.__len__()
            for category in all_finished_books_list:
                for book in category:
                    if book[0].lower() == second_command.lower():
                        if selected_books.__contains__(""):
                            first_index_of_empty_book = selected_books.index("")
                            selected_books.insert(first_index_of_empty_book, book)
                        else:
                            selected_books.append(book)
                        left_selections -= 1
                        print("\n+ You have selected", '"' + book[0] + '"', "as your",
                              (selected_books.index(book) + 1).__str__() + ". book.")
                        break
            if selected_books.__len__() == starting_element_count:
                print("\n- We couldn't find any match in the database for the given bookName. Try again.")
        elif main_command == "/reselect":
            if second_command == "1":
                if selected_books.__len__() != 0:
                    if selected_books[0] != "":
                        selected_books[0] = ""
                        left_selections += 1
                        print("\n> You can now select the new book.")
                    else:
                        print("\n- You already emptied your first selection.")
                else:
                    print("\n- You didn't selected any book(s) yet.")
            elif second_command == "2":
                if selected_mode != 2:
                    print("\n- Your game mode is not allowing you for multiple book selections already.\n"
                          "- No need for reselecting the second book.")
                elif selected_mode == 2 and selected_books.__len__() != 0:
                    if selected_books[1] != "":
                        selected_books[1] = ""
                        left_selections += 1
                        print("\n> You can now select the new book.")
                    else:
                        print("\n- You already emptied your second selection.")
                elif selected_mode == 2 and selected_books.__len__() == 0:
                    print("\n- You didn't selected any book(s) yet.")
            else:
                print("\n- Wrong reselect command entered.\n"
                      "> If you want to learn more about commands, write '/help' without the apostrophes.")
        elif command == "/change_mode":
            selected_books.clear()

            print("\n> To analyse two books to analyse:")
            print("- Please enter 'Y'")
            print("\n> To analyse only one book:")
            print("- Please enter 'N'\n")
            get_mode_input()

            print("+ The mode has been changed.")

            left_selections = selected_mode
        elif command == "/analyse" and left_selections == 0:
            loop_ended = True
        elif command == "/analyse" and left_selections != 0:
            print("\n- You didn't select enough books.\n"
                  "> If you want to learn more about commands, write '/help' without the apostrophes.")
        elif main_command == "/restart":
            print("\n- You can only restart when analysis complete.\n"
                  "> If you want to learn more about commands, write '/help' without the apostrophes.")
        else:
            print("\n- Wrong command entered.\n"
                  "> If you want to learn more about commands, write '/help' without the apostrophes.")

        if left_selections == 0 and loop_ended is False:
            print("\n"
                  "> If you are happy with your selections, you can start analysing book(s) with '/analyse' command.\n"
                  "> If you want to change the book(s), use '/reselect' command variations.\n"
                  "> If you want to change the mode, use '/change_mode' command variations.\n"
                  "\n> If you want to learn more about commands, write '/help' without the apostrophes.")


# Scrapes Wikibooks for Book List From Direct User Input #
def web_scraping_and_selection_from_direct_user_input():
    print("\n> To analyse two books at once:")
    print("- Please enter 'Y'")
    print("\n> To analyse only one book:")
    print("- Please enter 'N'\n")
    get_mode_input()

    if selected_mode == 1:
        # Variables #
        true_input = False

        while true_input is False:
            # Variables #
            url_exists = False
            right_format = False

            book_name_input = input("< Please enter the book's name (case sensitive): ")

            only_book_name = book_name_input.encode('utf-8').decode().replace("'", "%27")

            url_extension_to_book = "/wiki/" + only_book_name.replace(" ", "_")

            try:
                url_extension_to_book.encode('ascii')
                right_format = True
            except UnicodeEncodeError:
                print("\n- Please only use English for book names. Try again.\n")

            if right_format:
                try:
                    check_if_downloadable_object_book = urllib.request.urlopen(
                        "https://en.wikibooks.org" + url_extension_to_book)
                    url_exists = True
                except urllib.error.HTTPError:
                    print("\n- Either the book you chose is not valid or it "
                          "doesn't have a printable version. Try again.\n")

                if url_exists:
                    check_if_downloadable_book = check_if_downloadable_object_book.read()

                    check_if_downloadable_book_str = check_if_downloadable_book.decode("utf-8")

                    check_if_downloadable_book_str = str.replace(check_if_downloadable_book_str, "\n", "")

                    downloadable = check_if_downloadable_book_str.__contains__(
                        url_extension_to_book + "/Print_version")

                    if downloadable:
                        true_input = True
                        selected_books.append([book_name_input, url_extension_to_book, "DI000"])
                        print("\n+ You have selected", '"' + book_name_input + '"', "as your book. Please wait for the "
                                                                                    "export process.\n")
                    else:
                        print("\n- Either the book you chose is not valid or it "
                              "doesn't have a printable version. Try again.\n")
    else:
        # Variables #
        true_input01 = False
        true_input02 = False

        while true_input01 is False:
            # Variables #
            url_exists = False
            right_format = False

            book_name_input = input("< Please enter the first book's name (case sensitive): ")

            only_book_name = book_name_input.encode('utf-8').decode().replace("'", "%27")

            url_extension_to_book = "/wiki/" + only_book_name.replace(" ", "_")

            try:
                url_extension_to_book.encode('ascii')
                right_format = True
            except UnicodeEncodeError:
                print("\n- Please only use English for book names. Try again.\n")

            if right_format:
                try:
                    check_if_downloadable_object_book = urllib.request.urlopen(
                        "https://en.wikibooks.org" + url_extension_to_book)
                    url_exists = True
                except urllib.error.HTTPError:
                    print("\n- Either the book you chose is not valid or it "
                          "doesn't have a printable version. Try again.\n")

                if url_exists:
                    check_if_downloadable_book = check_if_downloadable_object_book.read()

                    check_if_downloadable_book_str = check_if_downloadable_book.decode("utf-8")

                    check_if_downloadable_book_str = str.replace(check_if_downloadable_book_str, "\n", "")

                    downloadable = check_if_downloadable_book_str.__contains__(
                        url_extension_to_book + "/Print_version")

                    if downloadable:
                        true_input01 = True
                        selected_books.append([book_name_input, url_extension_to_book, "DI000"])
                        print("\n+ You have selected", '"' + book_name_input + '"',
                              "as your first book. Please wait for the export process.\n")
                    else:
                        print("\n- Either the book you chose is not valid or it "
                              "doesn't have a printable version. Try again.\n")

        while true_input02 is False:
            # Variables #
            url_exists = False
            right_format = False

            book_name_input = input("< Please enter the second book's name (case sensitive): ")

            only_book_name = book_name_input.encode('utf-8').decode().replace("'", "%27")

            url_extension_to_book = "/wiki/" + only_book_name.replace(" ", "_")

            try:
                url_extension_to_book.encode('ascii')
                right_format = True
            except UnicodeEncodeError:
                print("\n- Please only use English for book names. Try again.\n")

            if right_format:
                try:
                    check_if_downloadable_object_book = urllib.request.urlopen(
                        "https://en.wikibooks.org" + url_extension_to_book)
                    url_exists = True
                except urllib.error.HTTPError:
                    print("\n- Either the book you chose is not valid or it "
                          "doesn't have a printable version. Try again.\n")

                if url_exists:
                    check_if_downloadable_book = check_if_downloadable_object_book.read()

                    check_if_downloadable_book_str = check_if_downloadable_book.decode("utf-8")

                    check_if_downloadable_book_str = str.replace(check_if_downloadable_book_str, "\n", "")

                    downloadable = check_if_downloadable_book_str.__contains__(
                        url_extension_to_book + "/Print_version")

                    if downloadable:
                        true_input02 = True
                        selected_books.append([book_name_input, url_extension_to_book, "DI999"])
                        print("\n+ You have selected", '"' + book_name_input + '"',
                              "as your second book. Please wait for the export process.\n")
                    else:
                        print("\n- Either the book you chose is not valid or it "
                              "doesn't have a printable version. Try again.\n")


# Scrapes Wikibooks for Printable Version of the book(s) and Writes Them to a File #
def web_scraping_for_print_version_and_io():
    # Global Variables #
    global selected_mode
    global selected_books

    for index in range(selected_mode):
        print("> Downloading, filtering and exporting '" + selected_books[index][0] + "'.")
        print_version_of_book_url = "https://en.wikibooks.org" + selected_books[index][1] + "/Print_version"

        with open(selected_books[index][0] + '.txt', 'w', encoding='utf-8') as outfile:
            website = urllib.request.urlopen(print_version_of_book_url).read()
            site = BeautifulSoup(website, "html.parser")
            soup = site.find("div", {"class": "mw-parser-output"})
            unwanted = site.find("table", {"class": "metadata plainlinks ambox ambox-notice"})
            visible_text = soup.getText().replace(unwanted.getText(), "")
            print(visible_text, file=outfile)

        print("\n+ Finished.\n")


# Analysis for One Book #
def analyse_book_for_mode_1():
    # Global Variables #
    global selected_books
    global english_stop_words

    # Lists #
    found_word_list = ["-"]
    found_frequency_list = [0]

    # Variables #
    output_size = 20
    punctuation = "!#$%^&*()_<>?:.,;=\"{[]}\\£#$/-'"

    print("> Importing data...\n")

    book = open(selected_books[0][0] + ".txt", "r", encoding="utf-8").read()
    book = book.lower()
    for c in book:
        if c in punctuation:
            book = book.replace(c, " ")
    words_list_old_raw = re.findall(r'([^\s]+)', book)
    words_list_raw = re.findall(r'([^\s]+)', book)

    for word in words_list_old_raw:
        for stop_word in english_stop_words:
            if word == stop_word:
                words_list_raw.remove(word)

    words_list = []

    for word in words_list_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            words_list.append(word)

    # PROGRESS BAR INDICATORS #
    print("+ Successfully imported data. The analysis will begin after you choose the data output size.")
    print("- If you enter an empty input, the default value will be selected for the data output size. (20)\n")

    true_input = False
    output_size_input = input("< Data output size: ")

    if output_size_input == "":
        output_size = 20
        print("\n+ Data output size set to " + output_size.__str__() + "\n")
    else:
        while not true_input:
            try:
                output_size = int(output_size_input)
            except ValueError:
                output_size_input = input("\n< Data output size (Only Integers): ")
            else:
                true_input = True
                print("\n+ Data output size set to " + output_size.__str__() + "\n")

    print("- Analysis started...\n")

    print("> |" + 27 * "-" + "|" +
          "  " + "0" + "%" + "     "
          + "Current the most frequent word is: " + found_word_list[0] +
          " with " + found_frequency_list[0].__str__() + " times.", end="")

    increment = 100 / words_list.__len__()
    current_percent = 0

    eliminated_word_list = []
    eliminated_frequency_list = []

    for word in words_list:
        found_in_main_list = False
        eliminated_list_index = 0
        added_to_eliminate = False

        if word != "" and word in found_word_list:
            found_frequency_list[found_word_list.index(word)] += 1
            found_in_main_list = True
        else:
            found_word_list.append(word)
            found_frequency_list.append(1)

        if found_in_main_list is False and len(found_word_list) == output_size + 1:
            added_to_eliminate = True

            if word != "" and word in eliminated_word_list:
                eliminated_frequency_list[eliminated_word_list.index(word)] += 1
                eliminated_list_index = eliminated_word_list.index(word)
            else:
                eliminated_word_list.append(word)
                eliminated_frequency_list.append(1)

        if len(found_word_list) > output_size:
            found_frequency_list.pop()
            found_word_list.pop()

        if added_to_eliminate is True and found_in_main_list is False and len(found_word_list) == output_size:
            if eliminated_frequency_list[eliminated_list_index] > found_frequency_list[output_size - 1]:
                eliminated_temp_freq = eliminated_frequency_list[eliminated_list_index]
                eliminated_temp_word = eliminated_word_list[eliminated_list_index]

                eliminated_frequency_list[eliminated_list_index] = found_frequency_list[output_size - 1]
                eliminated_word_list[eliminated_list_index] = found_word_list[output_size - 1]

                found_frequency_list[output_size - 1] = eliminated_temp_freq
                found_word_list[output_size - 1] = eliminated_temp_word

        found_word_list_len = len(found_word_list)

        for i in range(found_word_list_len):
            for j in range(found_word_list_len - 1):
                if found_frequency_list[j] < found_frequency_list[j + 1]:
                    temp_freq = found_frequency_list[j]
                    temp_word = found_word_list[j]

                    found_frequency_list[j] = found_frequency_list[j + 1]
                    found_word_list[j] = found_word_list[j + 1]

                    found_frequency_list[j + 1] = temp_freq
                    found_word_list[j + 1] = temp_word

        for b in range(0, 105):
            print("\b", end="")

        current_percent += increment
        progress_bar_indicator = current_percent / 100 * 27

        print("> |" + (progress_bar_indicator.__int__()) * "#" + (27 - progress_bar_indicator.__int__()) * "-"
              + "|" + "  " + "%.2f" % current_percent + "%" + "   " +
              "Current the most frequent word is: '" + found_word_list[0] +
              "' with " + found_frequency_list[0].__str__() + " times.", end="")

    print("\n\n> BOOK 1: '" + selected_books[0][0] + "'" +
          "\n\n          ANALYSIS          " +
          "\n-  NO  BOOK        FREQUENCY")

    for index in range(len(found_word_list)):
        order: str
        word: str
        frequency: str

        if index + 1 < 10:
            order = "  " + (index + 1).__str__()
        elif 10 <= index + 1 < 100:
            order = " " + (index + 1).__str__()
        else:
            order = (index + 1).__str__()

        word = found_word_list[index] + (12 - found_word_list[index].__len__()) * " "

        frequency = found_frequency_list[index].__str__()

        print("- " + order + "  " + word + frequency)


# Analysis for Two Books For Common Words #
def analyse_book_for_mode_2_common():
    # Global Variables #
    global selected_books
    global english_stop_words

    # Variables #
    output_size = 20
    punctuation = "!#$%^&*()_<>?:.,;=\"{[]}\\£#$/-'"

    print("> Importing data...\n")

    book = open(selected_books[0][0] + ".txt", "r", encoding="utf-8").read()
    book = book.lower()
    for c in book:
        if c in punctuation:
            book = book.replace(c, " ")
    words_list_old_raw = re.findall(r'([^\s]+)', book)
    words_list_raw = re.findall(r'([^\s]+)', book)

    for word in words_list_old_raw:
        for stop_word in english_stop_words:
            if word == stop_word:
                words_list_raw.remove(word)

    words_list = []

    for word in words_list_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            words_list.append(word)

    book02 = open(selected_books[1][0] + ".txt", "r", encoding="utf-8").read()
    book02 = book02.lower()
    for c in book02:
        if c in punctuation:
            book02 = book02.replace(c, " ")
    words_list_old02_raw = re.findall(r'([^\s]+)', book02)
    words_list02_raw = re.findall(r'([^\s]+)', book02)

    for word in words_list_old02_raw:
        for stop_word in english_stop_words:
            if word == stop_word:
                words_list02_raw.remove(word)

    words_list02 = []

    for word in words_list02_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            words_list02.append(word)

    print("+ Successfully retrieved data. The analysis will begin after you choose the data output size.")
    print("- If you enter an empty input, the default value will be selected for the data output size. (20)\n")

    true_input = False
    output_size_input = input("< Data output size: ")

    if output_size_input == "":
        output_size = 20
        print("\n+ Data output size set to " + output_size.__str__() + "\n")
    else:
        while not true_input:
            try:
                output_size = int(output_size_input)
            except ValueError:
                output_size_input = input("\n< Data output size (Only Integers): ")
            else:
                true_input = True
                print("\n+ Data output size set to " + output_size.__str__() + "\n")

    common_words_list = list(set(words_list).intersection(words_list02))

    found_common_word_list01, found_common_frequency_list01 = common_or_distinct_words_lister(common_words_list,
                                                                                              words_list)

    found_common_word_list02, found_common_frequency_list02 = common_or_distinct_words_lister(common_words_list,
                                                                                              words_list02)

    total_count_of_common_words_list: list = ["-"]
    total_count_of_common_frequency_list: list = [0]

    # PROGRESS BAR INDICATORS #

    print("- Analysis started...\n")

    print("> |" + 27 * "-" + "|" + "  " + "0" + "%" + "     "
          + "Current the most frequent common word is: " + total_count_of_common_words_list[0] +
          " with " + total_count_of_common_frequency_list[0].__str__() + " times.", end="")

    increment = 100 / common_words_list.__len__()
    current_percent = 0

    eliminated_common_word_list: list = []
    eliminated_common_frequency_list: list = []

    for word in common_words_list:
        added_to_eliminate = False
        eliminated_list_index = 0
        total_count = 0

        for index in range(len(found_common_word_list01)):
            if word == found_common_word_list01[index]:
                total_count += found_common_frequency_list01[index]
        for index in range(len(found_common_word_list02)):
            if word == found_common_word_list02[index]:
                total_count += found_common_frequency_list02[index]

        total_count_of_common_words_list.append(word)
        total_count_of_common_frequency_list.append(total_count)

        if len(total_count_of_common_words_list) == output_size + 1:
            added_to_eliminate = True

            if word != "":
                eliminated_common_word_list.append(word)
                eliminated_common_frequency_list.append(total_count)
                eliminated_list_index = eliminated_common_word_list.index(word)

        if len(total_count_of_common_words_list) > output_size:
            total_count_of_common_frequency_list.pop()
            total_count_of_common_words_list.pop()

        if added_to_eliminate is True and len(total_count_of_common_words_list) == output_size:
            if eliminated_common_frequency_list[eliminated_list_index] > \
                    total_count_of_common_frequency_list[output_size - 1]:
                eliminated_temp_freq = eliminated_common_frequency_list[eliminated_list_index]
                eliminated_temp_word = eliminated_common_word_list[eliminated_list_index]

                eliminated_common_frequency_list[eliminated_list_index] = total_count_of_common_frequency_list[
                    output_size - 1]
                eliminated_common_word_list[eliminated_list_index] = total_count_of_common_words_list[output_size - 1]

                total_count_of_common_frequency_list[output_size - 1] = eliminated_temp_freq
                total_count_of_common_words_list[output_size - 1] = eliminated_temp_word

        found_word_list_len = len(total_count_of_common_words_list)

        for i in range(found_word_list_len):
            for j in range(found_word_list_len - 1):
                if total_count_of_common_frequency_list[j] < total_count_of_common_frequency_list[j + 1]:
                    temp_freq = total_count_of_common_frequency_list[j]
                    temp_word = total_count_of_common_words_list[j]

                    total_count_of_common_frequency_list[j] = total_count_of_common_frequency_list[j + 1]
                    total_count_of_common_words_list[j] = total_count_of_common_words_list[j + 1]

                    total_count_of_common_frequency_list[j + 1] = temp_freq
                    total_count_of_common_words_list[j + 1] = temp_word

        # PROGRESS BAR #

        for b in range(0, 150):
            print("\b", end="")

        current_percent += increment
        progress_bar_indicator = current_percent / 100 * 27

        print(
            "> |" + (progress_bar_indicator.__int__() + 1) * "#" + (
                    26 - progress_bar_indicator.__int__()) * "-"
            + "|" + "  " + "%.2f" % current_percent + "%" + "   " +
            "Current the most frequent common word is: '" + total_count_of_common_words_list[0] +
            "' with " + total_count_of_common_frequency_list[0].__str__() + " times.", end="")

    print("\n\n> BOOK 1: '" + selected_books[0][0] + "'" +
          "\n> BOOK 2: '" + selected_books[1][0] + "'" +
          "\n\n                   COMMON WORDS                  " +
          "\n-  NO  BOOK        FREQ_1     FREQ_2     FREQ_SUM")

    for index in range(len(total_count_of_common_words_list)):
        order: str
        word: str
        frequency: str
        frequency2: str
        total_frequency: str

        if index + 1 < 10:
            order = "  " + (index + 1).__str__()
        elif 10 <= index + 1 < 100:
            order = " " + (index + 1).__str__()
        else:
            order = (index + 1).__str__()

        word = total_count_of_common_words_list[index] + \
               (12 - total_count_of_common_words_list[index].__len__()) * " "

        frequency = words_list.count(total_count_of_common_words_list[index]).__str__() + \
                    (11 - words_list.count(total_count_of_common_words_list[index]).__str__().__len__()) * " "

        frequency2 = words_list02.count(total_count_of_common_words_list[index]).__str__() + \
                     (11 - words_list02.count(total_count_of_common_words_list[index]).__str__().__len__()) * " "

        total_frequency = total_count_of_common_frequency_list[index].__str__() + \
                          (12 - total_count_of_common_frequency_list[index].__str__().__len__()) * " "

        print("- " + order + "  " + word + frequency + frequency2 + total_frequency)

    print("\n- Analysis started...")

    return output_size


# Analysis for Two Books For Distinct Words #
def analyse_book_for_mode_2_distinct(output_size_special: int):
    # Global Variables #
    global selected_books
    global english_stop_words

    # Variables #
    punctuation = "!#$%^&*()_<>?:.,;=\"{[]}\\£#$/-'"

    book = open(selected_books[0][0] + ".txt", "r", encoding="utf-8").read()
    book = book.lower()
    for c in book:
        if c in punctuation:
            book = book.replace(c, " ")
    words_list_old_raw = re.findall(r'([^\s]+)', book)
    words_list_raw = re.findall(r'([^\s]+)', book)

    for word in words_list_old_raw:
        for stop_word in english_stop_words:
            if word == stop_word:
                words_list_raw.remove(word)

    words_list = []

    for word in words_list_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            words_list.append(word)

    book02 = open(selected_books[1][0] + ".txt", "r", encoding="utf-8").read()
    book02 = book02.lower()
    for c in book02:
        if c in punctuation:
            book02 = book02.replace(c, " ")
    words_list_old02_raw = re.findall(r'([^\s]+)', book02)
    words_list02_raw = re.findall(r'([^\s]+)', book02)

    for word in words_list_old02_raw:
        for stop_word in english_stop_words:
            if word == stop_word:
                words_list02_raw.remove(word)

    words_list02 = []

    for word in words_list02_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            words_list02.append(word)

    common_words_list_raw = list(set(words_list).intersection(words_list02))
    common_words_list = []

    for word in common_words_list_raw:
        if word.isdecimal():
            word = ""
        if word.__len__() == 1 and word.isalnum():
            word = ""
        if word != "":
            common_words_list.append(word)

    for book_number in range(2):
        # Lists
        eliminated_word_list = []
        eliminated_frequency_list = []

        real_words_list = []

        if book_number == 0:
            for word in words_list:
                if word not in common_words_list:
                    real_words_list.append(word)
        else:
            for word in words_list02:
                if word not in common_words_list:
                    real_words_list.append(word)

        found_word_list = ["-"]
        found_frequency_list = [0]

        for word in real_words_list:
            found_in_main_list = False
            eliminated_list_index = 0
            added_to_eliminate = False

            if word != "" and word in found_word_list:
                found_frequency_list[found_word_list.index(word)] += 1
                found_in_main_list = True
            else:
                found_word_list.append(word)
                found_frequency_list.append(1)

            if found_in_main_list is False and len(found_word_list) == output_size_special + 1:
                added_to_eliminate = True

                if word != "" and word in eliminated_word_list:
                    eliminated_frequency_list[eliminated_word_list.index(word)] += 1
                    eliminated_list_index = eliminated_word_list.index(word)
                else:
                    eliminated_word_list.append(word)
                    eliminated_frequency_list.append(1)

            if len(found_word_list) > output_size_special:
                found_frequency_list.pop()
                found_word_list.pop()

            if added_to_eliminate is True and found_in_main_list is False and len(
                    found_word_list) == output_size_special:
                if eliminated_frequency_list[eliminated_list_index] > found_frequency_list[output_size_special - 1]:
                    eliminated_temp_freq = eliminated_frequency_list[eliminated_list_index]
                    eliminated_temp_word = eliminated_word_list[eliminated_list_index]

                    eliminated_frequency_list[eliminated_list_index] = found_frequency_list[output_size_special - 1]
                    eliminated_word_list[eliminated_list_index] = found_word_list[output_size_special - 1]

                    found_frequency_list[output_size_special - 1] = eliminated_temp_freq
                    found_word_list[output_size_special - 1] = eliminated_temp_word

            found_word_list_len = len(found_word_list)

            for i in range(found_word_list_len):
                for j in range(found_word_list_len - 1):
                    if found_frequency_list[j] < found_frequency_list[j + 1]:
                        temp_freq = found_frequency_list[j]
                        temp_word = found_word_list[j]

                        found_frequency_list[j] = found_frequency_list[j + 1]
                        found_word_list[j] = found_word_list[j + 1]

                        found_frequency_list[j + 1] = temp_freq
                        found_word_list[j + 1] = temp_word

        print("\n> BOOK " + book_number.__str__() + ": '" + selected_books[book_number][0] + "'" +
              "\n\n       DISTINCT WORDS       " +
              "\n-  NO  BOOK        FREQUENCY")

        for index in range(len(found_word_list)):
            order: str
            word: str
            frequency: str

            if index + 1 < 10:
                order = "  " + (index + 1).__str__()
            elif 10 <= index + 1 < 100:
                order = " " + (index + 1).__str__()
            else:
                order = (index + 1).__str__()

            word = found_word_list[index] + (12 - found_word_list[index].__len__()) * " "

            frequency = found_frequency_list[index].__str__()

            print("- " + order + "  " + word + frequency)


# Finds Common Items #
def common_item_finder(l1, l2):
    res = []
    for x in l1:
        if x in l2:
            res.append(x)
            l2.remove(x)
    return res


def common_or_distinct_words_lister(common_or_distinct_words_list: list, words_list: list):
    found_word_list = ["-"]
    found_frequency_list = [0]

    for word in words_list:
        if common_or_distinct_words_list.__contains__(word):

            if word != "" and word in found_word_list:
                found_frequency_list[found_word_list.index(word)] += 1
            else:
                found_word_list.append(word)
                found_frequency_list.append(1)

    return found_word_list, found_frequency_list


# Getting The Book List #
def end_screen():
    loops = False
    ended = False
    while not ended:
        print("\n- Since the analysis is finished, only '/help' and '/restart' commands can be used.")
        print("> If you need help with WFAT commands, enter '/help' to get command manual.")
        command = input("\n< Command: ")

        if command == "/help":
            print("\n#############################################################################################\n"
                  "|                                    WFAT COMMAND MANUAL                                    |\n"
                  "|       WFAT (Word Frequency Analysis Tool) commands are the dedicated way to control       |\n"
                  "|        this software. You can list, select and analyse the books with the commands.       |\n"
                  "|                         All commands start with the backslash '/'                         |\n"
                  "|                                                                                           |\n"
                  "|                                   ### COMMANDS LIST ###                                   |\n"
                  "|   |--------------------------ACTION-------------------------| |--------COMMAND--------|   |\n"
                  "|                                                                                           |\n"
                  "|   1. '/help' command variations:                                                          |\n"
                  "|   - To read the manual of WFAT commands:                       /help                      |\n"
                  "|                                                                                           |\n"
                  "|   2. '/list' command variations (If you haven't already decided your book(s).):           |\n"
                  "|   - To list all books:                                         /list all                  |\n"
                  "|   - To list the books that starts with numbers:                /list category_num         |\n"
                  "|   - To list the books that starts with 'A':                    /list category_a           |\n"
                  "|   - To list the books that starts with 'B':                    /list category_b           |\n"
                  "|   - ...                                                                                   |\n"
                  "|   - ..                                                                                    |\n"
                  "|   - .                                                                                     |\n"
                  "|                                                                                           |\n"
                  "|   3. '/select' command variations (Listed books will have identity numbers 'idNumber'):   |\n"
                  "|   - To select the book with its identity number:               /select_id idNumber        |\n"
                  "|   - To select the book with its name:                          /select_name bookName      |\n"
                  "|                                                                                           |\n"
                  "|   4. '/reselect' command variations:                                                      |\n"
                  "|   - To reselect the book 1 that you have selected:             /reselect 1                |\n"
                  "|   - To reselect the book 2 that you have selected:             /reselect 2                |\n"
                  "|                                                                                           |\n"
                  "|   5. '/change_mod' command variations (This will reset the current selected book(s):      |\n"
                  "|   - To change the current mode to single book analysis:        /change_mode 1             |\n"
                  "|   - To change the current mode to multiple book analysis:      /change_mode 2             |\n"
                  "|                                                                                           |\n"
                  "|   6. '/analyse' command variations:                                                       |\n"
                  "|   - To start analysing the book(s) you have selected:          /analyse                   |\n"
                  "|                                                                                           |\n"
                  "|   7. '/restart' command variations:                                                       |\n"
                  "|   - To enable loop for WFAT:                                   /restart true              |\n"
                  "|   - To disable loop for WFAT:                                  /restart false             |\n"
                  "|                                                                                           |\n"
                  "#############################################################################################"
                  )
        elif command == "/restart true":
            loops = True
            ended = True
        elif command == "/restart false":
            loops = False
            ended = True
        else:
            print("\n- Wrong command entered.\n"
                  "> If you want to learn more about commands, write '/help' without the apostrophes.")

    return loops


will_loop = True

while will_loop:
    ask_if_the_user_knows_the_books_already()

    if using_database is True:
        web_scraping_and_selection_from_database()
    else:
        web_scraping_and_selection_from_direct_user_input()

    web_scraping_for_print_version_and_io()

    if selected_mode == 1:
        analyse_book_for_mode_1()
    elif selected_mode == 2:
        source_output_size = analyse_book_for_mode_2_common()
        analyse_book_for_mode_2_distinct(source_output_size)

    will_loop = end_screen()
