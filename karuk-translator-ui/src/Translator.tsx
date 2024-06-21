import React, { useState } from 'react';

// Assuming the translateToKaruk function is imported from another file
import { translateToKaruk } from './translate';

const Translator: React.FC = () => {
    const [englishText, setEnglishText] = useState<string>('');
    const [karukText, setKarukText] = useState<string>('');
    const [loading, setLoading] = useState<boolean>(false);

    const handleTranslate = async () => {
        setLoading(true);
        try {
            const translation = await translateToKaruk(englishText);
            setKarukText(translation);
        } catch (error) {
            console.error("Translation error:", error);
            setKarukText("Error translating text.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
            <h1>English to Karuk Translator</h1>
            <textarea
                value={englishText}
                onChange={(e) => setEnglishText(e.target.value)}
                placeholder="Enter English text here..."
                disabled={loading}
                style={{ width: '100%', height: '100px', marginBottom: '10px' }}
            />
            <button
                onClick={handleTranslate}
                disabled={loading || !englishText.trim()}
                style={{ marginBottom: '10px', padding: '10px', width: '100%' }}
            >
                {loading ? 'Translating...' : 'Translate'}
            </button>
            {loading && <div>Loading...</div>}
            <textarea
                value={karukText}
                readOnly
                placeholder="Karuk translation will appear here..."
                style={{ width: '100%', height: '100px' }}
            />
        </div>
    );
};

export default Translator;
