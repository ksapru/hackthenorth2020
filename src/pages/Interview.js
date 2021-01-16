import React from 'react'
import Webcam from "react-webcam"

export default function Interview() {
    const videoConstraints = {
        width: 575,
        height: 375,
        mirrored: true,
        facingMode: "user"
    };

    return (
        <div>
            <Webcam
                style={{
                    position: 'absolute', left: '50%', top: '57%',
                    transform: 'translate(-50%, -50%)'
                }}
                audio={true}
                videoConstraints={videoConstraints}
            />
        </div>
    )
}
