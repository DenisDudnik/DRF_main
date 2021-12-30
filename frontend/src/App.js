import React from 'react';
import logo from './logo.svg';
import './App.css';
import './style.css'
import AuthorList from './components/Author.js'
import MenuList from './components/Menu.js'
import FooterContent from './components/Footer.js'

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'menuItems': [],
            'footerContent': [],
        }
    }

    componentDidMount() {
        const authors = [
            {
                'first_name': 'Фёдор',
                'last_name': 'Достоевский',
                'birthday_year': 1821
            },
            {
                'first_name': 'Александр',
                'last_name': 'Грин',
                'birthday_year': 1880
            },
        ]

        const menuItems = [
            {
                'title': 'Главная',
                'link': '/'
            },
            {
                'title': 'Настройки',
                'link': '/settings'
            },
        ]

        const footerContent = [
            {
                'owner': 'Denis.Dudnik@gmail.com',
                'year': (new Date()).getFullYear()
            },
        ]

        this.setState(
            {
                'authors': authors,
                'menuItems': menuItems,
                'footerContent': footerContent,
            }
        )
    }

    render() {
        return (
            <div class="wrapper">
                <div class="top">
                    <div class="main_blocks_container">
                        <div class="left_block">
                            <div class="menu">
                                <MenuList menuItems={this.state.menuItems} />
                            </div>
                        </div>
                        <div class="right_block">
                            <div class="content">
                                <AuthorList authors={this.state.authors} />
                            </div>
                        </div>
                    </div>
                </div>

                <div class="footer">
                    <FooterContent footerContent={this.state.footerContent} />
                </div>
            </div>
        )
    }
}

export default App;
