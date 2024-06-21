import { OpenAI } from "openai";

import translations from "./translations.json";

export async function translateToKaruk(text: string): Promise<string> {
    let apiKey = localStorage.getItem('openai_key');
    if (!apiKey) {
        apiKey = prompt('Please enter your OpenAI API key:');
        if (apiKey) {
            localStorage.setItem('openai_key', apiKey);
        } else {
            throw new Error('OpenAI API key not found in localStorage.');
        }
    }

    const configuration = {
        apiKey: apiKey,
        dangerouslyAllowBrowser: true,
    };

    const openai = new OpenAI(configuration);

    const messages = [
        {
            role: "system",
            content: "You are a translator who can translate English text into the Karuk language. Here are some example translations to guide you.",
        },
        ...translations.map(t => ({
            role: "system",
            content: `English: ${t.english}\nKaruk: ${t.karuk}`
        })),
        {
            role: "user",
            content: `Translate the following text to Karuk:\n${text}`,
        }
    ];

    const response = await openai.chat.completions.create({
        model: 'gpt-4o',
        messages: messages as any,
        max_tokens: 150,
        temperature: 0.7,
    });

    if (!response.choices || response.choices.length === 0) {
        throw new Error('No response from OpenAI API.');
    }
    if (!response.choices[0].message || !response.choices[0].message.content) {
        throw new Error('No response content from OpenAI API.');
    }
    return response.choices[0].message.content
}