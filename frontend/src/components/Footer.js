import React from 'react'


const FooterContent = ({ footerContent }) => {
    return (
        <span>Copyright &copy; {footerContent[0].owner} , {footerContent[0].year}</span>
    )
}


export default FooterContent