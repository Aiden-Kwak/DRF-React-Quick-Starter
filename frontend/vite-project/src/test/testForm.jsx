import axios from 'axios';
import React, { useState } from 'react';

function testForm() {
    const [message, setMessage] = useState("Type 'Biden' or 'Trump'.");
    const [receivedMessage, setReceivedMessage] = useState("");
    const [typedMessage, setTypedMessage] = useState("");

    const postVote = () => {
        axios.post('http://localhost:8000/api/test/post-vote', {
            message: typedMessage
        })
            .then((response) => {
                setReceivedMessage(response.data.message);
                setMessage(receivedMessage);
            })
            .catch((error) => {
                setMessage(error.message);
            });
    };

    const getVoteNum = () => {
        axios.get('http://localhost:8000/api/test/get-vote')
            .then((response) => {
                setReceivedMessage(response.data.message);
                setMessage(receivedMessage);
            })
            .catch((error) => {
                setMessage(error.message);
            });
    };

    return (
        <div>
            <h1>Test Form: Vote for Biden or Trump!</h1>

        </div>
    );

}

export default testForm;