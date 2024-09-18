
const createUser = async (req, res) => {
    const { username, email, password } = req.body;
    
}

const getUsers = async (req, res) => {
    // retrieve users from mongoDB

}

module.exports = {
    createUser,
    getUsers
}